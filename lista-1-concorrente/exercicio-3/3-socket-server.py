import socket
import threading

class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("New connection added: ", clientAddress)

    def run(self):
        while True:
            # Receives the first grade from the client
            grade_N1 = float(self.csocket.recv(1024).decode())
            # Sends the same data back for confirmation
            self.csocket.send(("RECEIVED " + str(grade_N1)).encode())

            # Receives the second grade from the client
            grade_N2 = float(self.csocket.recv(1024).decode())
            # Sends the same data back for confirmation
            self.csocket.send(("RECEIVED " + str(grade_N2)).encode())

            avg = (grade_N1 + grade_N2)/2

            if avg > 3 and avg < 7:
                self.csocket.send(("NEED THE THIRD GRADE!").encode())
                # Receives the third grade from the client
                grade_N3 = float(self.csocket.recv(1024).decode())
                # Sends the same data back for confirmation
                self.csocket.send(("RECEIVED " + str(grade_N3)).encode())

                total_avg = (avg + grade_N3)/2

                if total_avg >= 5:
                    self.csocket.send(("Aprovado(a)!").encode())
                else:
                    self.csocket.send(("Reprovado(a)!").encode())

            elif avg >= 7: 
                self.csocket.send(("Aprovado(a)!").encode())

            elif avg <= 3: 
                self.csocket.send(("Reprovado(a)!").encode())
            break
        print("Client at ", clientAddress, " disconnected...")

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