import socket

server_socket = socket.socket() # Creates network socket
server_socket.bind(("127.0.0.1", 12345)) # Socket's IP and network port
server_socket.listen() # Socket waits for client connections
client_connection, client_address = server_socket.accept() # When a client connects, the socket accepts the connection
print ("Socket Up and running with a connection from",client_address)

average_balance = client_connection.recv(1024).decode() # Receives last year's average balance from the client
client_connection.send(("RECEIVED " + average_balance).encode()) # Sends the same data back for confirmation

average_balance = float(average_balance) # string to float
credit = 0 # default condition (average_balance >= 0 and average_balance <= 200)

if average_balance >= 201 and average_balance <= 400:
    credit = float(average_balance * 0.2)

elif average_balance >= 401 and average_balance <= 600:
    credit = float(average_balance * 0.3)

elif average_balance > 601:
    credit = float(average_balance * 0.4)

final_response = "Average balance: $" + "{:.2f}".format(average_balance) + " | Credit: $" + "{:.2f}".format(credit) + "." # floats to string with 2 decimal places

client_connection.send(final_response.encode()) # Sends client's credit
    
client_connection.close()
server_socket.close()