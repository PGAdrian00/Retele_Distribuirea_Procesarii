import socket
import threading

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

is_running = True
stop_server = False
clients = []
clients_lock = threading.Lock()
DISCONNECT_MESSAGE ='q'

def handle_client(client_socket, client_address):
    with client_socket:
        while True:
            data = client_socket.recv(1024)
            if not data:
                with clients_lock:
                    clients.remove(client_address)
                print(f"[USER {client_address[0]}, {client_address[1]}] disconnected")
                break
            message = data.decode()
            if message == DISCONNECT_MESSAGE:
                with clients_lock:
                    clients.remove(client_address)
                print(f"[USER {client_address[0]}, {client_address[1]}] requested disconnection")
                close_all_clients()
                break
            print(f"[USER {client_address[0]}, {client_address[1]}] sent: {message}")
            # Process the task here and send back the result if needed

            if stop_server:
                break

def close_all_clients():
    global stop_server
    with clients_lock:
        for client_address in clients:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                try:
                    client_socket.connect((client_address[0], client_address[1]))
                    client_socket.sendall(b'DISCONNECT')
                except:
                    pass
    stop_server = True


def accept_connections(server_socket):
    while is_running:
        client_socket, client_address = server_socket.accept()
        with clients_lock:
            clients.append(client_address)
        print(f"[NEW CONNECTION] {client_address[0]}, {client_address[1]} connected")
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

def main():
    try:
        print("[STARTING] Server is starting...")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((SERVER_HOST, SERVER_PORT))
            server_socket.listen()
            print(f"[LISTENING] Server is listening on {SERVER_HOST}:{SERVER_PORT}")
            accept_thread = threading.Thread(target=accept_connections, args=(server_socket,))
            accept_thread.start()
            accept_thread.join()

            while not stop_server:
                pass  # Server is still running

    except Exception as e:
        print(f"An error occurred: {e}")

    print("[SERVER CLOSED] Server is no longer accepting connections")

if __name__ == '__main__':
    main()
