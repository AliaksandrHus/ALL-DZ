import socket
import time
import random

HOST = '127.0.0.1'
PORT = 8008

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:

        time.sleep(1)

        start = mess = random.choice(['виски # id:1', 'кола # id:1', 'лед # id:1'])
        mess = mess.encode('utf-8')
        s.sendall(mess)
        data = s.recv(1024)
        print(f'Отправлено: {start.split("#")[0]} / Получено: {data.decode("utf-8").split("#")[0]}')
