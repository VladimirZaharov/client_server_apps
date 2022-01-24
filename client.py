import sys
import threading
from socket import socket, AF_INET, SOCK_STREAM
from utils import send_msg, load_config, load_args, take_msg


def user_messenger(socket):
    while True:
        msg = input("Введите сообщение('exit' для выхода): ")
        if msg == 'exit':
            socket.close
            sys.exit(0)
        send_msg(msg, socket)


def main():
    configs = load_config()
    args = load_args(configs)
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((args.a, args.p))

    receiver = threading.Thread(target=take_msg, args=(s))
    receiver.daemon = True
    receiver.start()

    user_interface = threading.Thread(target=user_messenger, args=(s))
    user_interface.daemon = True
    user_interface.start()


if __name__ == '__main__':
    main()


