import socket

SERVER = "127.0.0.1"
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

while True:
    name = input("Enter your name: ")
    client.send(name.encode())
    print("SERVER RESPONSE: " + client.recv(1024).decode())

    level = input("Enter your level (A, B, C, D): ")
    client.send(level.encode())
    print("SERVER RESPONSE: " + client.recv(1024).decode())

    salary = input("Enter your salary: ")
    client.send(salary.encode())
    print("SERVER RESPONSE: " + client.recv(1024).decode())

    number_of_dependents = input("Enter the number of dependents: ")
    client.send(number_of_dependents.encode())
    print("SERVER RESPONSE: " + client.recv(1024).decode())

    print("SERVER RESPONSE: " + client.recv(1024).decode())

    break
client.close()
