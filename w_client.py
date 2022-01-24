import sys
from socket import socket, AF_INET, SOCK_STREAM
from utils import send_msg, load_config, load_args


def main():
    configs = load_config()
    args = load_args(configs)
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((args.a, args.p))
    while True:
        msg = input("Введите сообщение('exit' для выхода): ")
        if msg == 'exit':
            s.close
            sys.exit(0)
        send_msg(msg, s)

if __name__ == '__main__':
    main()
