import socket

server_socket = socket.socket() # Creates network socket
server_socket.bind(("127.0.0.1", 12345)) # Socket's IP and network port
server_socket.listen() # Socket waits for client connections
# When a client connects, the socket accepts the connection
client_connection, client_address = server_socket.accept()
print("Socket Up and running with a connection from", client_address)

# Receives the swimmer age from the client
swimmer_age = client_connection.recv(1024).decode()
# Sends the same data back for confirmation
client_connection.send(swimmer_age.encode())

swimmer_age = int(swimmer_age)
swimmer_category = ""

if swimmer_age >= 18:
    swimmer_category = "Adults"

elif swimmer_age >= 14:
    swimmer_category = "Youth B"

elif swimmer_age >= 11:
    swimmer_category = "Youth A"

elif swimmer_age >= 8:
    swimmer_category = "Children B"

elif swimmer_age >= 5:
    swimmer_category = "Children A"

else:
    swimmer_category = "None"

final_response = "Your category is: " + swimmer_category + "."

client_connection.send(final_response.encode())

client_connection.close()
server_socket.close()
