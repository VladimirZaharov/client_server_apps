from socket import socket, AF_INET, SOCK_STREAM
from utils import send_msg, take_msg, load_config, load_args
import time
from logs.client_log_config import logger


def gen_msg(user_name, action):
    msg = {
        "ACTION": action,
        "TIME": time.time(),
        "USER": {
            "ACCOUNT_NAME": user_name,
            "STATUS": "Yep, I am here!"
        }
    }
    return msg


def main():
    configs = load_config()
    args = load_args(configs)
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((args.a, args.p))
    send_msg(gen_msg('Vladimir', 'presence'), s)
    msg_from_server = take_msg(s)
    logger.info(f'server answered: {msg_from_server["ALERT"]}')
    s.close()
    return msg_from_server


if __name__ == '__main__':
    main()
