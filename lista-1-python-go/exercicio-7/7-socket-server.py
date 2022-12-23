import socket

server_socket = socket.socket()  # Creates network socket
server_socket.bind(("127.0.0.1", 12345))  # Socket's IP and network port
server_socket.listen()  # Socket waits for client connections
# When a client connects, the socket accepts the connection
client_connection, client_address = server_socket.accept()
print("Socket Up and running with a connection from", client_address)

# Receives the employee name from the client
name = client_connection.recv(1024).decode()
# Sends the same data back for confirmation
client_connection.send(("RECEIVED " + name).encode())

# Receives the employee level from the client
age = client_connection.recv(1024).decode()
# Sends the same data back for confirmation
client_connection.send(("RECEIVED " + age).encode())

# Receives the employee number of dependents from the client
service_time = client_connection.recv(1024).decode()
# Sends the same data back for confirmation
client_connection.send(("RECEIVED " + service_time).encode())

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
     client_connection.send(("Employee: " + str(name) + " can retire").encode())
else:
     client_connection.send(("Employee: " + str(name) + " cannot retire yet").encode())

client_connection.close()
server_socket.close()
