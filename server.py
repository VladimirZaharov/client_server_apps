import select
from socket import socket, AF_INET, SOCK_STREAM
from utils import load_config, load_args
from logs.server_log_config import logger


def read_msg(w_clients, all_clients):
    responses = {}
    for sock in w_clients:
        try:
            data = sock.recv(1024).decode('utf-8')
            responses[sock] = data
        except:
            logger.info(f'client disconnected')
            all_clients.remove(sock)
    return responses


def send_answer(requests, r_clients, all_clients):
    for sock in r_clients:
        if sock in requests:
            try:
                resp = requests[sock].encode('utf-8')
                sock.send(resp)
            except:
                logger.info(f'client disconnected')
                sock.close()
                all_clients.remove(sock)


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
            client_messages = read_msg(w, clients)
            if client_messages:
                try:
                    send_answer(client_messages, r, clients)
                except:
                    print('ошибка отправки')
    except OSError:
        logger.error('OS error')


if __name__ == '__main__':
    main()
    print('сервер остановлен')
