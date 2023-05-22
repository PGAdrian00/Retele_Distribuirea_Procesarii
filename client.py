import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

def register_with_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        client_socket.sendall(b'REGISTER')
        print("[CLIENT REGISTERED] Registered with the server")

def close_application():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        client_socket.sendall(b'CLOSE')
        print("[APPLICATION CLOSED] Closed the application")

def send_task(task_code, *args):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        task_message = f'TASK#{task_code}#{",".join(args)}'.encode()
        client_socket.sendall(task_message)
        print(f"[TASK SENT] Task {task_code} sent to the server")

def main():
    register_with_server()

    while True:
        task_code = input("Enter the task code (or 'q' to quit): ")
        if task_code.lower() == 'q':
            close_application()
            break
        args = input("Enter the arguments (comma-separated): ").split(',')
        send_task(task_code, *args)

if __name__ == '__main__':
    main()
