import socket
import json

HOST="127.0.0.1"
PORT=65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    print(f"[*] In ascolto su {HOST,PORT}")
    clientsocket,address=s.accept()
    contatore=0
    with clientsocket as cs:
        while True:
            contatore=contatore+1
            data=cs.recv(1024)
            if not data:
                break
            data=data.decode()
            data=json.loads(data)
            if data=="KO":
                break
            ris=f"Ciao, {address}. Ho ricevuto un messagio da te : {contatore}){data}\n"
            cs.sendall(ris.encode("UTF-8"))
        