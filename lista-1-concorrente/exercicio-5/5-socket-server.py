import socket
import threading

class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("New connection added: ", clientAddress)

    def run(self):
        while True:
            swimmer_age = self.csocket.recv(1024).decode()
            self.csocket.send(("RECEIVED " + swimmer_age).encode())

            self.verify_swimmer_category(swimmer_age)
            break
        print("Client at ", clientAddress, " disconnected...")

    def verify_swimmer_category(self, swimmer_age):
        swimmer_age = int(swimmer_age)
        swimmer_category = ""

        if swimmer_age >= 18:
            swimmer_category = "Adults"

        elif swimmer_age >= 14:
            swimmer_category = "Youth B"

        elif swimmer_age >= 11:
            swimmer_category = "Youth A"

        elif swimmer_age >= 8:
            swimmer_category = "Children B"

        elif swimmer_age >= 5:
            swimmer_category = "Children A"

        else:
            swimmer_category = "None"

        final_response = "Your category is: " + swimmer_category + "."

        self.csocket.send(final_response.encode())

LOCALHOST = "127.0.0.1"
PORT = 5566

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")

while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()