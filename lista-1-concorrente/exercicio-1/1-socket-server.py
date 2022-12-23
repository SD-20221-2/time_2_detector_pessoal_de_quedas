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
            employee_name = self.csocket.recv(1024).decode()
            # Sends the same data back for confirmation
            self.csocket.send(("RECEIVED " + employee_name).encode())

            # Receives the employee position from the client
            employee_position = self.csocket.recv(1024).decode()
            # Sends the same data back for confirmation
            self.csocket.send(("RECEIVED " + employee_position).encode())

            # Receives the employee salary from the client
            employee_salary = self.csocket.recv(1024).decode()
            # Sends the same data back for confirmation
            self.csocket.send(("RECEIVED " + employee_salary).encode())

            self.new_salary(employee_name, employee_position, employee_salary)
            break
        print("Client at ", clientAddress, " disconnected...")

    def new_salary(self, employee_name, employee_position, employee_salary):
        employee_salary = float(employee_salary) # string to float
        self.employee_new_salary = 0

        if employee_position == "operador":
            self.employee_new_salary = float(employee_salary * 1.2)

        elif employee_position == "programador":
            self.employee_new_salary = float(employee_salary * 1.18)

        final_response = employee_name + "'s new salary is $" + "{:.2f}".format(self.employee_new_salary) + "." # float to string with 2 decimal places

        self.csocket.send(final_response.encode()) # Sends the updated salary

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
    print(newthread)
    newthread.start()
    print(newthread)