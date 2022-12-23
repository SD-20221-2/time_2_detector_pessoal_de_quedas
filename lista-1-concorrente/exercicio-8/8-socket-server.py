import socket
import threading

class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("New connection added: ", clientAddress)

    def run(self):
        while True:
            # Receives last year's average balance from the client
            average_balance = self.csocket.recv(1024).decode()
            # Sends the same data back for confirmation
            self.csocket.send(("RECEIVED " + average_balance).encode())

            self.get_credit(average_balance)
            break
        print("Client at ", clientAddress, " disconnected...")

    def get_credit(self, average_balance):
        average_balance = float(average_balance) # string to float
        credit = 0 # default condition (average_balance >= 0 and average_balance <= 200)

        if average_balance >= 201 and average_balance <= 400:
            credit = float(average_balance * 0.2)

        elif average_balance >= 401 and average_balance <= 600:
            credit = float(average_balance * 0.3)

        elif average_balance > 601:
            credit = float(average_balance * 0.4)

        final_response = "Average balance: $" + "{:.2f}".format(average_balance) + " | Credit: $" + "{:.2f}".format(credit) + "." # floats to string with 2 decimal places

        self.csocket.send(final_response.encode()) # Sends client's credit
    

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