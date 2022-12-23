package main

import (
	"fmt"
	"github.com/kolo/xmlrpc"
)

func main() {
	var swimmer_age string
	var remote_result any

	fmt.Println("Enter your age: ")
	fmt.Scanln(&swimmer_age)

	client, _ := xmlrpc.NewClient("http://localhost:8000/", nil)
	client.Call("verify_swimmer_category", []interface{}{swimmer_age}, &remote_result)

    fmt.Println(remote_result)
}