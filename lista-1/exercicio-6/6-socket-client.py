import socket

client_socket = socket.socket() # Creates network socket
client_socket.connect(('127.0.0.1',12345)) # Connects to server IP and port

name = input("Enter your name: ")
client_socket.send(name.encode())
print("SERVER RESPONSE: " + client_socket.recv(1024).decode())

level = input("Enter your level (A, B, C, D): ")
client_socket.send(level.encode())
print("SERVER RESPONSE: " + client_socket.recv(1024).decode())

salary = input("Enter your salary: ")
client_socket.send(salary.encode())
print("SERVER RESPONSE: " + client_socket.recv(1024).decode())

number_of_dependents = input("Enter the number of dependents: ")
client_socket.send(number_of_dependents.encode())
print("SERVER RESPONSE: " + client_socket.recv(1024).decode())

client_socket.send("CONFIRM".encode())
print("SERVER RESPONSE: " + client_socket.recv(1024).decode())

client_socket.close()
