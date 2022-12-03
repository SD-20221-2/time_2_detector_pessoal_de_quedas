import socket

server_socket = socket.socket()  # Creates network socket
server_socket.bind(("127.0.0.1", 12345))  # Socket's IP and network port
server_socket.listen()  # Socket waits for client connections
# When a client connects, the socket accepts the connection
client_connection, client_address = server_socket.accept()
print("Socket Up and running with a connection from", client_address)

# Receives the employee name from the client
person_name = client_connection.recv(1024).decode()
# Sends the same data back for confirmation
client_connection.send(("RECEIVED " + person_name).encode())
# Receives the employee position from the client
person_gender = client_connection.recv(1024).decode()
# Sends the same data back for confirmation
client_connection.send(("RECEIVED " + person_gender).encode())
# Receives the employee salary from the client
person_age = client_connection.recv(1024).decode()
# Sends the same data back for confirmation
client_connection.send(("RECEIVED " + person_age).encode())

if person_gender == "M" and float(person_age) >= 18:
    client_connection.send(("Já atingiu a maioridade!").encode())
elif person_gender == "M" and float(person_age) < 18:
    client_connection.send(
        ("Não atingiu a maioridade. Pessoas do sexo masculino só atingem aos 18 anos!").encode())


if person_gender == "F" and float(person_age) >= 21:
    client_connection.send(("Já atingiu a maioridade!").encode())
elif person_gender == "F" and float(person_age) < 21:
    client_connection.send(
        ("Não atingiu a maioridade. Pessoas do sexo feminino só atingem aos 21 anos!").encode())

client_connection.close()
server_socket.close()
