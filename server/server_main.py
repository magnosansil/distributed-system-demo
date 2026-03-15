import socket
import shutil

HOST = "localhost"
PORT = 5000

UPDATE_LIMIT = 3
update_count = 0

def replicate():
    shutil.copy("data/stocks_server.txt", "data/stocks_replica.txt")
    print("Replica synchronized!")

def update_stock():
    global update_count

    with open("data/stocks_server.txt", "r") as f:
        lines = f.readlines()

    new_lines = []

    for line in lines:
        name, price = line.split()
        price = float(price) + 1
        new_lines.append(f"{name} {price:.2f}\n")

    with open("data/stocks_server.txt", "w") as f:
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

        with open("data/stocks_server.txt") as f:
            data = f.read()

        conn.send(data.encode())

    elif request == "UPDATE":

        update_stock()
        conn.send("Update performed".encode())

    conn.close()