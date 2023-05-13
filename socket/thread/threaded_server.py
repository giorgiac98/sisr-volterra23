# example of a threaded server

import socket
import sys
import threading


def handle_client(conn, addr):
    with conn:
        print(f"Connected by {addr}")
        data = ''
        while not data:
            data = client_socket.recv(1024)
            print(f"Received {data!r}")
            client_socket.sendall(data)


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server is listening on {HOST}::{PORT}")
    while True:
        (client_socket, address) = s.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.start()
        print(f"Active Connections: {threading.activeCount() - 1}")
except KeyboardInterrupt:
    s.close()
    sys.exit()

