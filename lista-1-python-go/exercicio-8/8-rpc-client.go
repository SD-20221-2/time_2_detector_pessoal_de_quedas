package main

import (
	"fmt"
	"github.com/kolo/xmlrpc"
)

func main() {
	var average_balance string
	var result string

	fmt.Println("Enter last year's average balance: $")
	fmt.Scanln(&average_balance)

	client, _ := xmlrpc.NewClient("http://localhost:8000/", nil)
	client.Call("credit", []interface{}{average_balance}, &result)
	fmt.Printf(result) 
}