import select
import socket

sock = socket.socket()
sock.bind(('localhost', 8008))
sock.listen(5)
sock.setblocking(False)
inputs = [sock]
outputs = []
messages = {}

while True:

    reads, send, excepts = select.select(inputs, outputs, inputs)

    for conn in reads:
        if conn == sock:
            new_conn, client_addr = conn.accept()
            print('Клиент подключился.')
            new_conn.setblocking(False)
            inputs.append(new_conn)

        else:
            data = conn.recv(1024)
            if data:
                if messages.get(conn, None):
                    messages[conn].append(data)
                else:
                    messages[conn] = [data]
                if conn not in outputs:
                    outputs.append(conn)
            else:
                print('Клиент отключился.')
                if conn in outputs:
                    outputs.remove(conn)
                inputs.remove(conn)
                conn.close()
                del messages[conn]

    for conn in send:
        msg = messages.get(conn, None)
        if len(msg):
            temp = msg.pop(0).decode('utf-8')
            start, client = temp.split(' # ')
            temp = temp.split('#')
            temp[0] = temp[0].upper()
            fin = temp[0]
            temp = ' # '.join(temp)
            print(f'Клиент {client} / Вход: {start} / Выход: {fin}' )
            conn.send(temp.encode())
        else:
            outputs.remove(conn)

    for conn in excepts:
        print('Ошибка! Соединение завершено.')
        inputs.remove(conn)
        if conn in outputs:
            outputs.remove(conn)
        conn.close()
        del messages[conn]