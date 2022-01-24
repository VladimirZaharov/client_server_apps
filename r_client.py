from socket import socket, AF_INET, SOCK_STREAM
from utils import take_msg, load_config, load_args


def main():
    configs = load_config()
    args = load_args(configs)
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((args.a, args.p))
    msg_from_server = take_msg(s)
    print(msg_from_server)
    s.close()


if __name__ == '__main__':
    main()
