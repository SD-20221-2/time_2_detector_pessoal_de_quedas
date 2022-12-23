import socket
import threading

class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("New connection added: ", clientAddress)

    def run(self):
        while True:
           
           # Receives the employee name from the client
            name =  self.csocket.recv(1024).decode()
            # Sends the same data back for confirmation
            self.csocket.send(("RECEIVED " + name).encode())

            # Receives the employee level from the client
            level =  self.csocket.recv(1024).decode()
            # Sends the same data back for confirmation
            self.csocket.send(("RECEIVED " + level).encode())

            # Receives the employee salary from the client
            salary =  self.csocket.recv(1024).decode()
            # Sends the same data back for confirmation
            self.csocket.send(("RECEIVED " + salary).encode())

            # Receives the employee number of dependents from the client
            number_of_dependents =  self.csocket.recv(1024).decode()
            # Sends the same data back for confirmation
            self.csocket.send(("RECEIVED " + number_of_dependents).encode())

            self.new_salary(name, level, salary, number_of_dependents)
            break
        print("Client at ", clientAddress, " disconnected...")

    def new_salary(self, name, level, salary, number_of_dependents):
        
        salary = float(salary)
        number_of_dependents = float(number_of_dependents)

        percentage_discount = 0

        if level == "A" and number_of_dependents >= 1:
            percentage_discount = 8
        elif level == "A" and number_of_dependents >= 0:
            percentage_discount = 3

        elif level == "B" and number_of_dependents >= 1:
            percentage_discount = 10
        elif level == "A" and number_of_dependents >= 0:
            percentage_discount = 5

        elif level == "C" and number_of_dependents >= 1:
            percentage_discount = 15
        elif level == "C" and number_of_dependents >= 0:
            percentage_discount = 8

        elif level == "D" and number_of_dependents >= 1:
            percentage_discount = 17
        elif level == "D" and number_of_dependents >= 0:
            percentage_discount = 10

        
        new_salary = salary - ((salary*percentage_discount)/100)
        self.csocket.send(("Salary: " + str(new_salary)).encode())


LOCALHOST = "127.0.0.1"
PORT = 12345

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