import socket
from threading import Thread

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 3004 
sep = "<SEP>" 

client_sockets = set()
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(10)
print(f"[*] Joindre le serveur sur {SERVER_HOST}:{SERVER_PORT}")

def conn_client(cs):
    
    while True:
        try:
            msg = cs.recv(1024).decode()
        except Exception as e:
            print(f"[!] Une erreur s'est produite")
            client_sockets.remove(cs)
        else:
            msg = msg.replace(sep, ": ")
        for client_socket in client_sockets:
            client_socket.send(msg.encode())


while True:
    client_socket, client_address = s.accept()
    print(f"[+] {client_address} viens de se connecter !")
    client_sockets.add(client_socket)
    
    new = Thread(target=conn_client, args=(client_socket,))
    new.daemon = True
    new.start()

for cs in client_sockets:
    cs.close()

s.close()
