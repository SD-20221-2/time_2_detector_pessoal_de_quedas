import socket

server_socket = socket.socket()  # Creates network socket
server_socket.bind(("127.0.0.1", 12345))  # Socket's IP and network port
server_socket.listen()  # Socket waits for client connections
# When a client connects, the socket accepts the connection
client_connection, client_address = server_socket.accept()
print("Socket Up and running with a connection from", client_address)

# Receives the first grade from the client
grade_N1 = float(client_connection.recv(1024).decode())
# Sends the same data back for confirmation
client_connection.send(("RECEIVED " + str(grade_N1)).encode())
# Receives the second grade from the client
grade_N2 = float(client_connection.recv(1024).decode())
# Sends the same data back for confirmation
client_connection.send(("RECEIVED " + str(grade_N2)).encode())

avg = (grade_N1 + grade_N2)/2

if avg > 3 and avg < 7:
    client_connection.send(("NEED THE THIRD GRADE!").encode())
    # Receives the third grade from the client
    grade_N3 = float(client_connection.recv(1024).decode())
    # Sends the same data back for confirmation
    client_connection.send(("RECEIVED " + str(grade_N3)).encode())

    total_avg = (avg + grade_N3)/2

    if total_avg >= 5:
        client_connection.send(("Aprovado(a)!").encode())
    else:
        client_connection.send(("Reprovado(a)!").encode())

elif avg >= 7:
    client_connection.send(("Aprovado(a)!").encode())
    
elif avg <= 3:
    client_connection.send(("Reprovado(a)!").encode())

client_connection.close()
server_socket.close()