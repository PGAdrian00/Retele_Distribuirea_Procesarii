import socket

SERVERHOSTIP='127.0.0.1'
PORT = 12345
FORMAT ='utf-8'


def main():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVERHOSTIP, PORT))
    message = "Hello world!"
    while True:
        client.send(message.encode(FORMAT))
        data = client.recv(1024)
        print(f"[MESSAGE FROM SERVER]: {data.decode(FORMAT)}")
        continuare = input("\nVrei sa continui conexiunea cu serverul(d/n):")
        if continuare =='d':
            continue
        else:
            break
    client.close()

if __name__ == '__main__':
    main()

