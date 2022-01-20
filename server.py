import select
import time
from socket import socket, AF_INET, SOCK_STREAM
from utils import send_msg, take_msg, load_config, load_args
from logs.server_log_config import logger


def gen_answer(client_msg):
    answer = {
        "RESPONSE": 200,
        "TIME": time.time(),
        "ALERT": f'{client_msg["USER"]["ACCOUNT_NAME"]} knocked!'
    }
    if client_msg['ACTION'] == 'presence' and client_msg['TIME'] and client_msg['USER']['ACCOUNT_NAME']:
        return answer
    else:
        answer['RESPONSE'] = 400
        answer['ALERT'] = 'bad request'
        logger.error('Данные от клиента не пришли или пришли некорректно')
        return answer


def main():
    clients = []
    try:
        configs = load_config()
        args = load_args(configs)
        s = socket(AF_INET, SOCK_STREAM)
        s.bind((args.a, args.p))
        s.listen(configs['MAX_CONNECTIONS'])
        s.settimeout(configs['TIMEOUT'])

        while True:
            try:
                client, addr = s.accept()
            except OSError as e:
                pass
            else:
                print(f'Получен запрос на соединение')
                clients.append(client)
            finally:
                wait = 0
                r = []
                w = []
                try:
                    r, w, e = select.select(clients, clients, [], wait)
                except:
                    pass
            client_message = take_msg(r, clients)
            logger.info(f'{client_message["USER"]["ACCOUNT_NAME"]} send {client_message["ACTION"]} message')
            send_msg(gen_answer(client_message), client)
            client.close()
            requests = read_requests(r, clients)
            write_responses(requests, w, clients)

    except OSError:
        logger.error('OS error')


if __name__ == '__main__':
    main()
