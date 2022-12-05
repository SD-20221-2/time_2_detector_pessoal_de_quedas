import socket

client_socket = socket.socket() # Creates network socket
client_socket.connect(('127.0.0.1',12345)) # Connects to server IP and port

average_balance = input("Enter last year's average balance: $")
client_socket.send(average_balance.encode())
print("SERVER RESPONSE: " + client_socket.recv(1024).decode())

print("SERVER RESPONSE: " + client_socket.recv(1024).decode())

client_socket.close()