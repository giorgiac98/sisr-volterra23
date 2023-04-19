# echo-server.py

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    (client_socket, address) = s.accept()
    with client_socket:
        print(f"Connected by {address}")
        data = ''
        while not data:
            data = client_socket.recv(1024)
            print(f"Received {data!r}")
            client_socket.sendall(data)
