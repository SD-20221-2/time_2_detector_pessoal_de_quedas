import socket

server_socket = socket.socket() # Creates network socket
server_socket.bind(("127.0.0.1", 12345)) # Socket's IP and network port
server_socket.listen() # Socket waits for client connections
client_connection, client_address = server_socket.accept() # When a client connects, the socket accepts the connection
print ("Socket Up and running with a connection from",client_address)

employee_name = client_connection.recv(1024).decode() # Receives the employee name from the client
client_connection.send(("RECEIVED " + employee_name).encode()) # Sends the same data back for confirmation

employee_position = client_connection.recv(1024).decode() # Receives the employee position from the client
client_connection.send(("RECEIVED " + employee_position).encode()) # Sends the same data back for confirmation

employee_salary = client_connection.recv(1024).decode() # Receives the employee salary from the client
client_connection.send(("RECEIVED " + employee_salary).encode()) # Sends the same data back for confirmation
employee_salary = float(employee_salary) # string to float

number_of_dependents = client_connection.recv(1024).decode() # Receives the number of dependents from the client
client_connection.send(("RECEIVED " + number_of_dependents).encode()) # Sends the same data back for confirmation
number_of_dependents = float(number_of_dependents) # string to float

percentage_discount = 0

if employee_position == "A" and number_of_dependents >= 1:
     percentage_discount = 8
elif employee_position == "A" and number_of_dependents >= 0:
     percentage_discount = 3

elif employee_position == "B" and number_of_dependents >= 1:
     percentage_discount = 10
elif employee_position == "A" and number_of_dependents >= 0:
     percentage_discount = 5

elif employee_position == "C" and number_of_dependents >= 1:
     percentage_discount = 15
elif employee_position == "C" and number_of_dependents >= 0:
     percentage_discount = 8

elif employee_position == "D" and number_of_dependents >= 1:
     percentage_discount = 17
elif employee_position == "D" and number_of_dependents >= 0:
     percentage_discount = 10


new_salary = employee_salary - ((employee_salary*percentage_discount)/100)


final_response = employee_name + "'s new salary is $" + "{:.2f}".format(new_salary) + "." # float to string with 2 decimal places

client_connection.send(final_response.encode()) # Sends the updated salary
    
client_connection.close()
server_socket.close()