import socket
import time

HOST = "server"  # Docker Compose service name
PORT = 5000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        while True:
            try:
                s.connect((HOST, PORT))
                break
            except ConnectionRefusedError:
                print("Waiting for server to be ready...")
                time.sleep(1)
        
        for i in range(1, 6):
            message = f"Message {i}"
            print(f"Producer: Sending {message}")
            s.sendall(message.encode('utf-8'))
            time.sleep(1)  # Simulate some delay

if __name__ == "__main__":
    main()  