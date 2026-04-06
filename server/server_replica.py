import socket
from pathlib import Path

HOST = "0.0.0.0"
STOCKS_REPLICA = Path(__file__).resolve().parent.parent / "data" / "stocks_replica.txt"
PORT = 6000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Replica server running on port {PORT}")

while True:
    conn, addr = server.accept()

    request = conn.recv(1024).decode()

    if request == "GET_REPLICA":

        with open(STOCKS_REPLICA) as f:
            data = f.read()

        conn.send(data.encode())

    conn.close()