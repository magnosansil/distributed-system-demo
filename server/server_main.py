import socket
import shutil
from pathlib import Path

HOST = "0.0.0.0"
DATA_DIR = Path(__file__).resolve().parent.parent / "data"
STOCKS_SERVER = DATA_DIR / "stocks_server.txt"
STOCKS_REPLICA = DATA_DIR / "stocks_replica.txt"
PORT = 5000

UPDATE_LIMIT = 3
update_count = 0

def replicate():
    shutil.copy(STOCKS_SERVER, STOCKS_REPLICA)
    print("Replica synchronized!")

def update_stock():
    global update_count

    with open(STOCKS_SERVER, "r") as f:
        lines = f.readlines()

    new_lines = []

    for line in lines:
        name, price = line.split()
        price = float(price) + 1
        new_lines.append(f"{name} {price:.2f}\n")

    with open(STOCKS_SERVER, "w") as f:
        f.writelines(new_lines)

    update_count += 1

    print(f"Update performed ({update_count}/{UPDATE_LIMIT})")

    if update_count >= UPDATE_LIMIT:
        replicate()
        update_count = 0

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Main server running on port {PORT}")

while True:
    conn, addr = server.accept()
    request = conn.recv(1024).decode()

    if request == "GET_SERVER":

        with open(STOCKS_SERVER) as f:
            data = f.read()

        conn.send(data.encode())

    elif request == "UPDATE":

        update_stock()
        conn.send("Update performed".encode())

    conn.close()