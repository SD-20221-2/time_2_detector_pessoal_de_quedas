
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
               name = self.csocket.recv(1024).decode()
               # Sends the same data back for confirmation
               self.csocket.send(("RECEIVED " + name).encode())

               # Receives the employee level from the client
               age = self.csocket.recv(1024).decode()
               # Sends the same data back for confirmation
               self.csocket.send(("RECEIVED " + age).encode())

               # Receives the employee number of dependents from the client
               service_time = self.csocket.recv(1024).decode()
               # Sends the same data back for confirmation
               self.csocket.send(("RECEIVED " + service_time).encode())

               self.new_salary(name, age, service_time)
               break
          print("Client at ", clientAddress, " disconnected...")

    def new_salary(self, name, age, service_time):
        
          age = float(age)
          service_time = float(service_time)

          can_retire = 0

          if age >= 65: 
               can_retire = 1
          elif service_time >= 30:
               can_retire = 1
          elif age >= 60 and service_time >= 25:
               can_retire = 1
          else:
               can_retire = 0

          if can_retire == 1: 
               self.csocket.send(("Employee: " + str(name) + " can retire").encode())
          else:
               self.csocket.send(("Employee: " + str(name) + " cannot retire yet").encode())


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