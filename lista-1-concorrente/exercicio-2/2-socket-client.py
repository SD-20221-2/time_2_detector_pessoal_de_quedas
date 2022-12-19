import socket

SERVER = "127.0.0.1"
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

while True:
    person_name = input("Enter your name: ")
    client.send(person_name.encode())
    print("SERVER RESPONSE: " + client.recv(1024).decode())

    person_gender = input("Enter your gender (M for male | F for female): ")
    client.send(person_gender.encode())
    print("SERVER RESPONSE: " + client.recv(1024).decode())

    person_age = input("Enter your age: ")
    client.send(person_age.encode())
    print("SERVER RESPONSE: " + client.recv(1024).decode())

    print("SERVER RESPONSE: " + client.recv(1024).decode())
    break
client.close()