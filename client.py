import json
from pickle import TRUE
import socket  

HOST="127.0.0.1"
PORT=65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    while True:
        primoNumero=input("Inserisci il primo numero. exit() per uscire")
        if primoNumero=="exit()":
            break
        primoNumero=float(primoNumero)
        operazione=input("Inserisci l'operazione (+,-,*,/,%)")
        secondoNumero=float(input("Inserisci il secondo numero"))
        messaggio={
            'primoNumero':primoNumero,
            'operazione':operazione,
            'secondoNumero':secondoNumero
        }
        #Trasformiamo l'oggetto in una stringa
        messaggio=json.dumps(messaggio)
        s.sendall(messaggio.encode("UTF-8"))
        data=s.recv(1024)
        print("Risultato: ",data.decode()) 