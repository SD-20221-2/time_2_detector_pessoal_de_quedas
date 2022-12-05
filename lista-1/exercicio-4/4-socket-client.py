import socket

client_socket = socket.socket() # Creates network socket
client_socket.connect(('127.0.0.1', 12345)) # Connects to server IP and port

person_height = input("Enter your height (in centimeters): ")
client_socket.send(person_height.encode())
print("SERVER RESPONSE: " + client_socket.recv(1024).decode())

person_gender = input("Enter your gender (M for male | F for female): ")
client_socket.send(person_gender.encode())
print("SERVER RESPONSE: " + client_socket.recv(1024).decode())

client_socket.send("CONFIRM".encode())
print("SERVER RESPONSE: " + client_socket.recv(1024).decode())

client_socket.close()