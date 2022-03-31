#nome del file : pagellaClientMulti.py
import socket
import sys
import random
import os
import time
import threading
import multiprocessing
import json
import pprint

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22225
NUM_WORKERS=4

#Versione 1 
def genera_richieste1(num,address,port):
    try:
        s=socket.socket()
        s.connect((address,port))
        print(f"\n{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
    except:
        print(f"{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
        sys.exit()

    #1. Generazione casuale:
    #   di uno studente (valori ammessi: 5 cognomi a caso tra cui il tuo cognome)
    #   di una materia (valori ammessi: Matematica, Italiano, inglese, Storia e Geografia)
    #   di un voto (valori ammessi 1 ..10)
    #   delle assenze (valori ammessi 1..5)
    studenti=['Zaniolo','Rossi','Bianchi','Verdi','Colombo']
    materie=['Matematica','Italiano','Inglese','Storia','Geografia']
    voto=random.randint(1,10)
    assenze=random.randint(1,5)
    #2. comporre il messaggio, inviarlo come json
    #   esempio: {'studente': 'Studente4', 'materia': 'Italiano', 'voto': 2, 'assenze': 3}
    messaggio={
        'studente':studenti[random.randint(0,4)],
        'materia':materie[random.randint(0,4)],
        'voto':voto,
        'assenze':assenze
    }
    messaggio=json.dumps(messaggio)
    print('Invio dati : '+str(messaggio))
    s.sendall(messaggio.encode("UTF-8"))
    data=s.recv(1024)
    #3. ricevere il risultato come json: {'studente':'Studente4','materia':'italiano','valutazione':'Gravemente insufficiente'}
    if not data:
        print(f"{threading.current_thread().name}: Server non risponde. Exit")
    else:
    #4 stampare la valutazione ricevuta esempio: La valutazione di Studente4 in italiano è Gravemente insufficiente
        data=data.decode()
        data=json.loads(data)
        studente=data['studente']
        esito=data['esito']
        materia=data['materia']
        print(f"{threading.current_thread().name}: Risultato: Il voto dello studente {studente} in {materia} è {esito}") # trasforma il vettore di byte in stringa
    s.close()
        

#Versione 2 
def genera_richieste2(num,address,port):
  #....
    try:
        s=socket.socket()
        s.connect((address,port))
        print(f"\n{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
    except:
        print(f"{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
        sys.exit()
  #   1. Generazione casuale di uno studente(valori ammessi: 5 cognomi a caso scelti da una lista)
  #   Per ognuna delle materie ammesse: Matematica, Italiano, inglese, Storia e Geografia)
  #   generazione di un voto (valori ammessi 1 ..10)
  #   e delle assenze (valori ammessi 1..5) 
  #   esempio: pagella={"Cognome1":[("Matematica",8,1), ("Italiano",6,1), ("Inglese",9.5,3), ("Storia",8,2), ("Geografia",8,1)]}
    studenti=['Zaniolo','Rossi','Bianchi','Verdi','Colombo']
    studente=studenti[random.randint(0,4)]
    pagella=[
    ('Matematica',random.randint(1,10),random.randint(1,5)),
    ('Italiano',random.randint(1,10),random.randint(1,5)),
    ('Inglese',random.randint(1,10),random.randint(1,5)),
    ('Storia',random.randint(1,10),random.randint(1,5)),
    ('Geografia',random.randint(1,10),random.randint(1,5))]
  #2. comporre il messaggio, inviarlo come json
    messaggio={
        'pagella':pagella,
        'studente':studente
    }
    messaggio=json.dumps(messaggio)
    print('invio dati: '+str(pagella))
    s.sendall(messaggio.encode("UTF-8"))
    data=s.recv(1024)
  #3  ricevere il risultato come json {'studente': 'Cognome1', 'media': 8.0, 'assenze': 8}
    if not data:
        print(f"{threading.current_thread().name}: Server non risponde. Exit")
    else:
    #4 stampare la valutazione ricevuta esempio: La valutazione di Studente4 in italiano è Gravemente insufficiente
        data=data.decode()
        data=json.loads(data)
        studente=data['studente']
        media=data['media']
        assenze=data['assenze']
        print(f"{threading.current_thread().name}: Risultato: Lo studente {studente} ha una media di {media} e {assenze} assenze") # trasforma il vettore di byte in stringa
    s.close()

#Versione 3
def genera_richieste3(num,address,port):
  #....
  #   1. Per ognuno degli studenti ammessi: 5 cognomi a caso scelti da una lista
  #   Per ognuna delle materie ammesse: Matematica, Italiano, inglese, Storia e Geografia)
  #   generazione di un voto (valori ammessi 1 ..10)
  #   e delle assenze (valori ammessi 1..5) 
  #   esempio: tabellone={"Cognome1":[("Matematica",8,1), ("Italiano",6,1), ("Inglese",9,3), ("Storia",8,2), ("Geografia",8,1)],
  #                       "Cognome2":[("Matematica",7,2), ("Italiano",5,3), ("Inglese",4,12), ("Storia",5,2), ("Geografia",4,1)],
  #                        .....}
    try:
        s=socket.socket()
        s.connect((address,port))
        print(f"\n{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
    except:
        print(f"{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
        sys.exit()
    
  #2. comporre il messaggio, inviarlo come json
    studenti=['Zaniolo','Rossi','Bianchi','Verdi','Colombo']
    materie=['Matematica','Italiano','Inglese','Storia','Geografia']
    tabellone={}
    for stud in studenti:
        pagella=[]
        for m in materie:
            voto=random.randint(1,10)
            assenze=random.randint(1,5)
            pagella.append((m,voto,assenze))
        tabellone[stud]=pagella
    print("Dati inviati al server")
    tabellone=json.dumps(tabellone)
    s.sendall(tabellone.encode("UTF-8"))
  #3  ricevere il risultato come json e stampare l'output come indicato in CONSOLE CLIENT V.3
    data=s.recv(1024)
    data=data.decode()
    data=json.load(data)
    if not data:
        print(f"{threading.current_thread().name}: Server non risponde. Exit")
    else:
        for elemento in data:
           print(f"{threading.current_thread().name}: Risultato: Lo studente {elemento['studente']} ha una media di {elemento['media']} e {elemento['assenze']} assenze") # trasforma il vettore di byte in stringa
    s.close()

if __name__ == '__main__':
    start_time=time.time()
    # PUNTO A) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3)
    # alla quale passo i parametri (num,SERVER_ADDRESS, SERVER_PORT)
    # for i in range(NUM_WORKERS):
    #     genera_richieste1(i,address=SERVER_ADDRESS,port=SERVER_PORT)
    # end_time=time.time()
    # print("Total SERIAL time=", end_time - start_time)
     
    start_time=time.time()
    threads=[]
    # PUNTO B) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3)  
    # tramite l'avvio di un thread al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    # avviare tutti i thread e attenderne la fine
    for i in range(NUM_WORKERS):
        th=threading.Thread(target=genera_richieste2(i,SERVER_ADDRESS,SERVER_PORT))
        threads.append(th)
    # 5 avvio tutti i thread
    for thread in threads:
        thread.start()
    # 6 aspetto la fine di tutti i thread
    for thread in threads:
        thread.join()
    end_time=time.time()
    print("Total THREADS time= ", end_time - start_time)

    start_time=time.time()
    process=[]
    # PUNTO C) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3) 
    # tramite l'avvio di un processo al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    # avviare tutti i processi e attenderne la fine
    for i in range(NUM_WORKERS):
        process.append(multiprocessing.Process(target=genera_richieste1, args=(i,SERVER_ADDRESS,SERVER_PORT)))
        #process.append(multiprocessing.Process(target=genera_richieste2, args=(i,SERVER_ADDRESS,SERVER_PORT)))
        #process.append(multiprocessing.Process(target=genera_richieste3, args=(i,SERVER_ADDRESS,SERVER_PORT)))
    [process.start() for process in process]
    [process.join() for process in process]
    end_time=time.time()
    print("Total PROCESS time= ", end_time - start_time)