import socket

HOST = "localhost"

def get_server():

    s = socket.socket()
    s.connect((HOST, 5000))

    s.send("GET_SERVER".encode())

    data = s.recv(4096).decode()

    print("\nSERVER FILE:")
    print(data)

    s.close()


def get_replica():

    s = socket.socket()
    s.connect((HOST, 6000))

    s.send("GET_REPLICA".encode())

    data = s.recv(4096).decode()

    print("\nREPLICA FILE:")
    print(data)

    s.close()


def update_server():

    s = socket.socket()
    s.connect((HOST, 5000))

    s.send("UPDATE".encode())

    print(s.recv(1024).decode())

    s.close()


while True:

    print("\n1 - Download file from main server")
    print("2 - Download file from replica")
    print("3 - Update stock prices")
    print("4 - Exit")

    option = input("Choose: ")

    if option == "1":
        get_server()

    elif option == "2":
        get_replica()

    elif option == "3":
        update_server()

    elif option == "4":
        break