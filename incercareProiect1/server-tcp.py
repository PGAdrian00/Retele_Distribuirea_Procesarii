import socket
import threading

SERVERHOSTIP = '127.0.0.1' #cea mai utilizata adresa de loopback
PORT = 12345 #un port din cele disponibile pt customizat (>1023, 1023 de porturi sunt default, ex: 80 http, 443 https, 21 ftp, 22 ftps ,445 smb,.....)


is_running = True


def handle_client(client, addr):
    with client:
        while True:
            if client == None:
                break
            host,port=client.getpeername()
            data = client.recv(1024)
            print(f"USER[{host},{port}] sent : {data}")
            if not data:
                clients.remove(addr)
                print(f'[USER{host},{port}] bye')
                break
            client.sendall(data.capitalize())

clients=[]

def accept(server):
    while is_running:
        client, addr = server.accept()
        clients.append(addr)
        for clientLista in clients:
            print(f'[CLIENTS_CONNECTION_LIST]: {clientLista}')
        print(f"[NEW CONNECTION] {addr} has connected!")
        client_thread = threading.Thread(target=handle_client, args=(client, addr))
        client_thread.start()

def main():
    try:
        print("[STARTING] Server is starting...")
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # definire socket de tip tcp prin SOCK_STREAM
        server.bind((SERVERHOSTIP,PORT))
        server.listen()
        print(f"[LISTENING] Server is listening on {PORT}")
        accept_thread = threading.Thread(target= accept, args=(server,))
        accept_thread.start()
        accept_thread.join()


    except BaseException as err:
        print(err)
    finally:
        if server:
            server.close()

if __name__ == '__main__':
    main()
