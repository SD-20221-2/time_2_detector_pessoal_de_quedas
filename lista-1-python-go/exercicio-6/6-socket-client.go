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
	var employee_name string
	var employee_position string
	var employee_salary string
	var number_of_dependents string

	// establish connection
	connection, err := net.Dial(SERVER_TYPE, SERVER_HOST+":"+SERVER_PORT)

	if err != nil {
		panic(err)
	}

	fmt.Println("Enter the employee name: ")
	fmt.Scanln(&employee_name)
	fmt.Println("Enter the employee position: A, B, C or D")
	fmt.Scanln(&employee_position)
	fmt.Println("Enter the employee salary: $")
	fmt.Scanln(&employee_salary)
	fmt.Println("Enter the number of dependents: $")
	fmt.Scanln(&number_of_dependents)

	server_send(connection, err, employee_name)
	server_send(connection, err, employee_position)
	server_send(connection, err, employee_salary)
	server_send(connection, err, number_of_dependents)
	server_receive(connection, err)

	defer connection.Close()
}
