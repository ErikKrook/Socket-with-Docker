import socket

HOST = "0.0.0.0"  # Bind to all network interfaces
PORT = 5000       # Must match the client's PORT

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))  # Bind the server to the specified host and port
        s.listen()            # Listen for incoming connections
        print(f"Server is listening on {HOST}:{PORT}")
        
        conn, addr = s.accept()  # Accept a client connection
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)  # Receive up to 1024 bytes
                if not data:
                    break  # Break the loop if no more data is received
                print(f"Consumer: Received {data.decode('utf-8')}")

if __name__ == "__main__":
    main()
