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
    try:
        configs = load_config()
        args = load_args(configs)
        s = socket(AF_INET, SOCK_STREAM)
        s.bind((args.a, args.p))
        s.listen(configs['MAX_CONNECTIONS'])

        while True:
            client, addr = s.accept()
            client_message = take_msg(client)
            logger.info(f'{client_message["USER"]["ACCOUNT_NAME"]} send {client_message["ACTION"]} message')
            send_msg(gen_answer(client_message), client)
            client.close()
    except OSError:
        logger.error('OS error')


if __name__ == '__main__':
    main()
