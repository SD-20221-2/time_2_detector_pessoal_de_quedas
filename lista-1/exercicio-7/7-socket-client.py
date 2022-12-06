import socket

client_socket = socket.socket() # Creates network socket
client_socket.connect(('127.0.0.1',12345)) # Connects to server IP and port

name = input("Enter your name: ")
client_socket.send(name.encode())
print("SERVER RESPONSE: " + client_socket.recv(1024).decode())

age = input("Enter your age: ")
client_socket.send(age.encode())
print("SERVER RESPONSE: " + client_socket.recv(1024).decode())

service_time = input("Enter your service time: ")
client_socket.send(service_time.encode())
print("SERVER RESPONSE: " + client_socket.recv(1024).decode())

client_socket.send("CONFIRM".encode())
print("SERVER RESPONSE: " + client_socket.recv(1024).decode())

client_socket.close()
