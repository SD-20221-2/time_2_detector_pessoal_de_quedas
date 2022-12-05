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
level = client_connection.recv(1024).decode()
# Sends the same data back for confirmation
client_connection.send(("RECEIVED " + level).encode())

# Receives the employee salary from the client
salary = client_connection.recv(1024).decode()
# Sends the same data back for confirmation
client_connection.send(("RECEIVED " + salary).encode())

# Receives the employee number of dependents from the client
number_of_dependents = client_connection.recv(1024).decode()
# Sends the same data back for confirmation
client_connection.send(("RECEIVED " + number_of_dependents).encode())

salary = float(salary)
number_of_dependents = float(number_of_dependents)

percentage_discount = 0

if level == "A" and number_of_dependents >= 1:
     percentage_discount = 8
elif level == "A" and number_of_dependents >= 0:
     percentage_discount = 3

elif level == "B" and number_of_dependents >= 1:
     percentage_discount = 10
elif level == "A" and number_of_dependents >= 0:
     percentage_discount = 5

elif level == "C" and number_of_dependents >= 1:
     percentage_discount = 15
elif level == "C" and number_of_dependents >= 0:
     percentage_discount = 8

elif level == "D" and number_of_dependents >= 1:
     percentage_discount = 17
elif level == "D" and number_of_dependents >= 0:
     percentage_discount = 10


new_salary = salary - ((salary*percentage_discount)/100)
client_connection.send(("Salary: " + str(new_salary)).encode())

client_connection.close()
server_socket.close()
