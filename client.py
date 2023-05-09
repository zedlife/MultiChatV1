import socket
from threading import Thread
from datetime import datetime


SERVER_HOST = "127.0.0.1"
SERVER_PORT = 3004
sep = "<SEP>"

s = socket.socket()
print(f"[*] Connexion au serveur {SERVER_HOST}:{SERVER_PORT}...")

s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connexion reussi !")
pseudo = input("Choisissez votre pseudo dans le chat: ")

def ecoute_msg():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)


t = Thread(target=ecoute_msg)
t.daemon = True
t.start()

while True:
    to_send =  input()
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    if to_send.lower() == 'q':
        sorti=f"[{date_now}] {pseudo}{sep} est deconnecte du chat !"
        s.send(sorti.encode())
        break
    
    to_send = f"[{date_now}] {pseudo}{sep}{to_send}"
    s.send(to_send.encode())

s.close()
