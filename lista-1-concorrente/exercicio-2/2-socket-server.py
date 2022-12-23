import socket
import threading

class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("New connection added: ", clientAddress)

    def run(self):
        while True:
            # Receives the person name from the client
            person_name = self.csocket.recv(1024).decode()
            # Sends the same data back for confirmation
            self.csocket.send(("RECEIVED " + person_name).encode())

            # Receives the person gender from the client
            person_gender = self.csocket.recv(1024).decode()
            # Sends the same data back for confirmation
            self.csocket.send(("RECEIVED " + person_gender).encode())

            # Receives the person age from the client
            person_age = self.csocket.recv(1024).decode()
            # Sends the same data back for confirmation
            self.csocket.send(("RECEIVED " + person_age).encode())

            self.age_majority(person_name, person_gender, person_age)
            break
        print("Client at ", clientAddress, " disconnected...")

    def age_majority(self, person_name, person_gender, person_age):
        if person_gender == "M" and float(person_age) >= 18:
            self.csocket.send((person_name + " came of age!").encode())
        elif person_gender == "M" and float(person_age) < 18:
            self.csocket.send(
                (person_name + " didn't come of age. Males don't come of age until they are 18!").encode())
        elif person_gender == "F" and float(person_age) >= 21:
            self.csocket.send((person_name + " came of age!").encode())
        elif person_gender == "F" and float(person_age) < 21:
            self.csocket.send(
                (person_name + " didn't come of age. Females don't come of age until they are 21!").encode())

LOCALHOST = "127.0.0.1"
PORT = 8080

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