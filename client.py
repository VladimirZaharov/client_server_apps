from socket import socket, AF_INET, SOCK_STREAM
import time
import json
import sys


def send_msg(some_message, some_socket):
    msg_json = json.dumps(some_message)
    some_socket.send(msg_json.encode('utf-8'))


def take_msg(some_socket):
    answer_srv_json = some_socket.recv(1024).decode('utf-8')
    answer_srv = json.loads(answer_srv_json)
    return answer_srv


def main():
    addr = ''
    port = 7777
    if len(sys.argv) > 1:
        addr = sys.argv[1]
        port = sys.argv[2]
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((addr, port))

    account_name = 'Vladimir'
    presence_msg = {
        "action": "presence",
        "time": time.time(),
        "type": "status",
        "user": {
            "account_name": account_name,
            "status": "Yep, I am here!"
        }
    }

    send_msg(presence_msg, s)
    msg_from_server = take_msg(s)
    print(msg_from_server['alert'])
    s.close()
    return msg_from_server


if __name__ == '__main__':
    main()
