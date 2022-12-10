import socket

client_socket = socket.socket() # Creates network socket
client_socket.connect(('127.0.0.1',12345)) # Connects to server IP and port

employee_name = input("Enter the employee name: ")
client_socket.send(employee_name.encode())
print("SERVER RESPONSE: " + client_socket.recv(1024).decode())

employee_position = input("Enter the employee position: ")
client_socket.send(employee_position.encode())
print("SERVER RESPONSE: " + client_socket.recv(1024).decode())

employee_salary = input("Enter the employee salary: $")
client_socket.send(employee_salary.encode())
print("SERVER RESPONSE: " + client_socket.recv(1024).decode())

print("SERVER RESPONSE: " + client_socket.recv(1024).decode())

client_socket.close()