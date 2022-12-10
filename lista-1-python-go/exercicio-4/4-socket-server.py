import socket

server_socket = socket.socket() # Creates network socket
server_socket.bind(("127.0.0.1", 12345)) # Socket's IP and network port
server_socket.listen() # Socket waits for client connections
# When a client connects, the socket accepts the connection
client_connection, client_address = server_socket.accept()
print("Socket Up and running with a connection from", client_address)

# Receives the person height from the client
person_height = client_connection.recv(1024).decode()
# Sends the same data back for confirmation
client_connection.send(("RECEIVED " + person_height).encode())
# Receives the person gender from the client
person_gender = client_connection.recv(1024).decode()
# Sends the same data back for confirmation
client_connection.send(("RECEIVED " + person_gender).encode())

person_height = float(person_height) / 100.0
ideal_weight = 0.0

if person_gender == "M":
    ideal_weight = float((72.7 * person_height) - 58.0)

elif person_gender == "F":
    ideal_weight = float((62.1 * person_height) - 44.7)

final_response = "Your ideal weight is: " + "{:.2f}".format(ideal_weight) + " kg."

client_connection.send(final_response.encode())

client_connection.close()
server_socket.close()
