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
	buffer := make([]byte, 4096)
	mLen, err := connection.Read(buffer)
	if err != nil {
		fmt.Println("Error reading:", err.Error())
	}
	fmt.Println("Received: ", string(buffer[:mLen]))
}

func main() {
	var person_name string
	var person_gender string
	var person_age string

	// establish connection
	connection, err := net.Dial(SERVER_TYPE, SERVER_HOST+":"+SERVER_PORT)

	if err != nil {
		panic(err)
	}

	fmt.Println("Enter your name: ")
	fmt.Scanln(&person_name)
	fmt.Println("Enter your gender (M for male | F for female): ")
	fmt.Scanln(&person_gender)
	fmt.Println("Enter your age: ")
	fmt.Scanln(&person_age)

	server_send(connection, err, person_name)
	server_send(connection, err, person_gender)
	server_send(connection, err, person_age)
	server_receive(connection, err)
	defer connection.Close()
}
