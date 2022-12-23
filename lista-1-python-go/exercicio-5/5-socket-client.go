package main

import (
	"fmt"
	"net"
)

const (
	SERVER_HOST = "localhost"
	SERVER_PORT = "12345"
	SERVER_TYPE = "tcp"
)

func server_send(connection net.Conn, err error, message string) {
	_, err = connection.Write([]byte(message))
	buffer := make([]byte, 1024)
	mLen, err := connection.Read(buffer)
	if err != nil {
		fmt.Println("Error reading:", err.Error())
	}
	fmt.Println("Received: ", string(buffer[:mLen]))
}

func server_receive(connection net.Conn, err error) string {
	buffer := make([]byte, 4096)
	mLen, err := connection.Read(buffer)
	if err != nil {
		return string("Error reading:" + err.Error())
	}
	return string(buffer[:mLen])
}

func main() {
	var swimmer_age string
	var result string

	// establish connection
	connection, err := net.Dial(SERVER_TYPE, SERVER_HOST+":"+SERVER_PORT)

	if err != nil {
		panic(err)
	}

	fmt.Println("Enter your age: ")
	fmt.Scanln(&swimmer_age)

	server_send(connection, err, swimmer_age)
	result = server_receive(connection, err)

	fmt.Println(result)
	defer connection.Close()
}