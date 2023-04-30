import socket
import threading

SERVERHOSTIP='127.0.0.1'#adresa loopback





def handle_client(client_socket, client):
    with client:
        while True:
            if client == None:
                break
            data = client.recv(1024)
            if not data:
                break
            print(data)
            client_socket.sendall(data)
            dest_res = client_socket.recv(1024)
            if dest_res:
                client.sendall(dest_res)


clients = []
is_running = True
def process_connection(server_socket,client_socket):
    while is_running:
        client, addr = server_socket.accept()
        clients.append(addr)
        print(f'[CLIENT CONNECTED] {addr} has connected!YAY')
        client_thread = threading.Thread(target = handle_client, args=(client_socket, client))
        client_thread.start()
        client_thread.join()


def tunnel(source_port, destination_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#conexiune TCP STREAM
    try:
        server_socket.bind((SERVERHOSTIP, source_port))
        server_socket.listen()
        print(f'\n[SERVER STARTING] ServerSocket started for {source_port}')
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVERHOSTIP, destination_port))
        print(f'\n[CLIENTSOCKET CONNECTED] ClientSocket connected to {destination_port}')
        accept_thread = threading.Thread(target = process_connection, args=(server_socket, client_socket))
        accept_thread.start()
        accept_thread.join()
    except BaseException as err:
        print(err)
    finally:
        if server_socket:
            server_socket.close()



tunnels = []
def main():
    finished = False
    while not finished:
        #command = input('Write command (see help for assistance): ')
        command = input('<anything>[]<source_port>[]<destination_port> or write list: ')
        if command.strip()=='exit':
            #disconnect from server
            is_running=False
            finished=True
        else:
            # if command.strip() == 'help':
            #     print('List of commands format: ')
            #     print('<anything>[space]<source_port>[space]<destination_port> - for setting up server and client')
            #     print('list -> for printing list of clients')
            if command.strip() == 'list':
                print(f'[TUNNELS LIST] : {tunnels}')
            else:
                (_, source_port, destination_port)=command.strip().split(' ')
                tunnel_thread = threading.Thread(target=tunnel, args=(int(source_port), int(destination_port)))
                tunnel_thread.start()
                tunnels.append((source_port,destination_port))

if __name__=='__main__':
    main()