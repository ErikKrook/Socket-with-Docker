import socket
import time

HOST = "consumer"  # Docker Compose service name
PORT = 5000



def main():
    with socket.socket() as s:
        while True:
            try:
                print(f"host and port client {HOST}, {PORT}")
                s.connect((HOST, PORT))
                break
            except ConnectionRefusedError:
                print("Waiting for consumer to be ready...")
                time.sleep(1)
        
        for i in range(1, 6):
            message = f"Message {i}"
            print(f"Producer: Sending {message}")
            s.sendall(message.encode('utf-8'))
            time.sleep(1)  # Simulate some delay

if __name__ == "__main__":
    main()  