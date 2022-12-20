package main

import (
	"fmt"
	"time"
	"net"
)

const (
	SERVER_HOST = "localhost"
	SERVER_PORT = "5566"
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

func query_server(i int, person_height string, person_gender string) {
	connection, err := net.Dial(SERVER_TYPE, SERVER_HOST+":"+SERVER_PORT)

	if err != nil {
		panic(err)
	}

	server_send(connection, err, person_height)
    server_send(connection, err, person_gender)
    server_receive(connection, err)

	fmt.Println("QUERY ", i)

	defer connection.Close()
}

func main() {

	for i := 1; i <= 100; i++ {
		go query_server(i, "170", "M")
		time.Sleep(time.Millisecond / 2)
	}

	fmt.Println("END")
}