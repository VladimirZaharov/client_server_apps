import yaml
import json
import argparse
import sys
from logs.decorator_log import log_decorator


def load_args(confs):
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', default=confs['DEFAULT_PORT'])
    parser.add_argument('-a', default='')
    args = parser.parse_args(sys.argv[1:])
    return args


def load_config():
    with open('config.yaml', 'r') as config_file:
        configs = yaml.load(config_file, Loader=yaml.Loader)
    return configs


@log_decorator
def send_msg(some_message, some_socket):
    some_socket.send(some_message.encode('utf-8'))


@log_decorator
def take_msg(some_socket):
    msg = some_socket.recv(1024).decode('utf-8')
    return msg
