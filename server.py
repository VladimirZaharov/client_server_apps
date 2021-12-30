from socket import socket, AF_INET, SOCK_STREAM
import sys
import argparse
from client import send_msg, take_msg


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', default=7777)
    parser.add_argument('-a', default='')

    args = parser.parse_args(sys.argv[1:])

    s = socket(AF_INET, SOCK_STREAM)
    s.bind((args.a, args.p))
    s.listen(5)

    while True:
        client, addr = s.accept()
        print(take_msg(client)['user']['account_name'])

        answer_code = ''
        alert = 'ответ сервера'
        server_msg = {
            "response": answer_code,
            "alert": alert
            }
        send_msg(server_msg, client)
        client.close()


if __name__ == '__main__':
    main()
