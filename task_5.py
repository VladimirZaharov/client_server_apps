import subprocess

args_1 = ['ping', 'youtube.com']
args_2 = ['ping', 'yandex.ru']

def ping_sites(args):
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
                line = line.decode('cp866').encode('utf-8')
                print(line.decode('utf-8'))
    return subproc_ping

ping_sites(args_1)
ping_sites(args_2)