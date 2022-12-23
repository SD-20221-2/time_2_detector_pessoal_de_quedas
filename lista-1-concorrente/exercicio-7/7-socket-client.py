import socket

SERVER = "127.0.0.1"
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

while True:
    name = input("Enter your name: ")
    client.send(name.encode())
    print("SERVER RESPONSE: " + client.recv(1024).decode())

    age = input("Enter your age: ")
    client.send(age.encode())
    print("SERVER RESPONSE: " + client.recv(1024).decode())

    service_time = input("Enter your service time: ")
    client.send(service_time.encode())
    print("SERVER RESPONSE: " + client.recv(1024).decode())

    client.send("CONFIRM".encode())
    print("SERVER RESPONSE: " + client.recv(1024).decode())

    break
client.close()
