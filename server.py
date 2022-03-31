import socket
import json

HOST="127.0.0.1"
PORT=65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    print(f"[*] In ascolto su {HOST,PORT}")
    clientsocket,address=s.accept()
    with clientsocket as cs:
        print("Connessione da ",address)
        while True:
            data=cs.recv(1024)
            if not data:
                break
            print("sjehhfvrubrb")
            data=data.decode()
            data=json.loads(data)
            primoNumero=data['primoNumero']
            operazione=data['operazione']
            secondoNumero=data['secondoNumero']
            ris=""
            if operazione=="+":
                ris=primoNumero+secondoNumero
            elif operazione=="-":
                ris=primoNumero-secondoNumero
            elif operazione=="*":
                ris=primoNumero*secondoNumero
            elif operazione=="/" and secondoNumero!="0":
                ris=primoNumero/secondoNumero
            elif operazione=="%":
                ris=primoNumero%secondoNumero
            else:
                ris="Operazione non riconusciuta"
            ris=str(ris)
            cs.sendall(ris.encode("UTF-8"))