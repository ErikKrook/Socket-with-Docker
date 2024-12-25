import socket
import time

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    print(f"Client hostname: {host}")
    port = 5000  # socket server port number
    print(f"Connecting to Server at {host}:{port}")
    
    client_socket = socket.socket()  # instantiate
    print("Client socket created")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        while True:
            try:
                s.connect((host, port))
                print("Client: Connected to the server established")
                break
            except ConnectionRefusedError:
                print("Waiting for consumer to be ready...")
                time.sleep(1)
    
    message = input("Input: ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()




    