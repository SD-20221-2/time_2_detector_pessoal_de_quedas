import socket
import threading

class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("New connection added: ", clientAddress)

    def run(self):
        while True:
            person_height = self.csocket.recv(1024).decode()
            self.csocket.send(("RECEIVED " + person_height).encode())

            person_gender = self.csocket.recv(1024).decode()
            self.csocket.send(("RECEIVED " + person_gender).encode())

            self.calculate_ideal_weight(person_height, person_gender)
            break
        print("Client at ", clientAddress, " disconnected...")

    def calculate_ideal_weight(self, person_height, person_gender):
        person_height = float(person_height) / 100.0
        ideal_weight = 0.0

        if person_gender == "M":
            ideal_weight = float((72.7 * person_height) - 58.0)

        elif person_gender == "F":
            ideal_weight = float((62.1 * person_height) - 44.7)

        final_response = "Your ideal weight is: " + "{:.2f}".format(ideal_weight) + " kg."

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