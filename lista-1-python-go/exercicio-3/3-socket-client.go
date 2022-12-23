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
	var grade_N1 string
	var grade_N2 string
	var grade_N3 string
	var result string

	// establish connection
	connection, err := net.Dial(SERVER_TYPE, SERVER_HOST+":"+SERVER_PORT)

	if err != nil {
		panic(err)
	}

	fmt.Println("Enter the first grade: ")
	fmt.Scanln(&grade_N1)
	fmt.Println("Enter the second grade:")
	fmt.Scanln(&grade_N2)

	server_send(connection, err, grade_N1)
	server_send(connection, err, grade_N2)
	result = server_receive(connection, err)

	if result == "NEED THE THIRD GRADE!" {
		fmt.Println("Need to enter the third grade!")
		fmt.Println("Enter the third grade: ")
		fmt.Scanln(&grade_N3)
		server_send(connection, err, grade_N3)
		result = server_receive(connection, err)
	}

	fmt.Println(result)
	defer connection.Close()
}
