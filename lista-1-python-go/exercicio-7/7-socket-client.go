// socket-client project 1-socket-client.go
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

func server_receive(connection net.Conn, err error) {
	buffer := make([]byte, 1024)
	mLen, err := connection.Read(buffer)
	if err != nil {
		fmt.Println("Error reading:", err.Error())
	}
	fmt.Println("Received: ", string(buffer[:mLen]))
}

func main() {
	var name string
	var age string
	var service_time string

	// establish connection
	connection, err := net.Dial(SERVER_TYPE, SERVER_HOST+":"+SERVER_PORT)

	if err != nil {
		panic(err)
	}

	fmt.Println("Enter the employee name: ")
	fmt.Scanln(&name)
	fmt.Println("Enter the age: ")
	fmt.Scanln(&age)
	fmt.Println("Enter the service time: $")
	fmt.Scanln(&service_time)

	server_send(connection, err, name)
	server_send(connection, err, age)
	server_send(connection, err, service_time)
	server_receive(connection, err)

	defer connection.Close()
}