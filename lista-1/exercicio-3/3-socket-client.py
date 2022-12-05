import socket

client_socket = socket.socket()  # Creates network socket
client_socket.connect(('127.0.0.1', 12345))  # Connects to server IP and port

grade_N1 = input("Enter the first grade: ")
client_socket.send(grade_N1.encode())
print("SERVER RESPONSE: " + client_socket.recv(1024).decode())

grade_N2 = input("Enter the second grade: ")
client_socket.send(grade_N2.encode())
print("SERVER RESPONSE: " + client_socket.recv(1024).decode())

if client_socket.recv(1024).decode() == "NEED THE THIRD GRADE!":
    grade_N3 = input("Enter the third grade: ")
    client_socket.send(grade_N3.encode())
    print("SERVER RESPONSE: " + client_socket.recv(1024).decode())

client_socket.send("CONFIRM".encode())
print("SERVER RESPONSE: " + client_socket.recv(1024).decode())

client_socket.close()