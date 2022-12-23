import socket

SERVER = "127.0.0.1"
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

while True:
    grade_N1 = input("Enter the first grade: ")
    client.send(grade_N1.encode())
    print("SERVER RESPONSE: " + client.recv(1024).decode())

    grade_N2 = input("Enter the second grade: ")
    client.send(grade_N2.encode())
    print("SERVER RESPONSE: " + client.recv(1024).decode())

    if client.recv(1024).decode() == "NEED THE THIRD GRADE!":
        grade_N3 = input("Enter the third grade: ")
        client.send(grade_N3.encode())
        print("SERVER RESPONSE: " + client.recv(1024).decode())
     
    print("SERVER RESPONSE: " + client.recv(1024).decode())
    break
client.close()