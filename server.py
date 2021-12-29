from socket import socket, AF_INET, SOCK_STREAM
import json
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument ('-p', default=7777)
parser.add_argument('-a', default='')

args = parser.parse_args(sys.argv[1:])

s = socket(AF_INET, SOCK_STREAM)
s.bind((args.a, args.p))
s.listen(5)

while True:
    client,addr = s.accept()
    client_msg_json = client.recv(1024).decode('utf-8')
    client_msg = json.loads(client_msg_json)
    print(client_msg['user']['account_name'])

    answer_code = ''
    alert = 'ответ сервера'
    server_msg = {
        "response": answer_code,
        "alert": alert
        }
    server_msg_json = json.dumps(server_msg)
    client.send(server_msg_json.encode('utf-8'))
    client.close()