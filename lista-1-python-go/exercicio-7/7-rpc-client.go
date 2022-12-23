package main

import (
	"fmt"
	"github.com/kolo/xmlrpc"
)

func main() {
	var name string
	var age string
	var service_time string
	var result string

	fmt.Println("Enter your name: ")
	fmt.Scanln(&name)
	fmt.Println("Enter the age: ")
	fmt.Scanln(&age)
	fmt.Println("Enter the service time: $")
	fmt.Scanln(&service_time)

	client, _ := xmlrpc.NewClient("http://localhost:8000/", nil)
	client.Call("can_retire", []interface{}{name, age, service_time}, &result)
	fmt.Printf(result) 
}
