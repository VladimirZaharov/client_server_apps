from socket import socket, AF_INET, SOCK_STREAM
import time
import json
import sys

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
                "account_name":  account_name,
                "status":      "Yep, I am here!"
        }
}
presence_msg_json = json.dumps(presence_msg)
s.send(presence_msg_json.encode('utf-8'))

answer_srv_json = s.recv(1024).decode('utf-8')
answer_srv = json.loads(answer_srv_json)
print(answer_srv['alert'])
s.close()