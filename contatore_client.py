import json
from pickle import TRUE
import socket  

HOST="127.0.0.1"
PORT=65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    while True:
        messaggio=input("Inserisci messaggio(KO se vuoi interrompere la connessione")
        #Trasformiamo l'oggetto in una stringa
        messaggio=json.dumps(messaggio)
        s.sendall(messaggio.encode("UTF-8"))
        data=s.recv(1024)
        print("Risultato: ",data.decode()) 