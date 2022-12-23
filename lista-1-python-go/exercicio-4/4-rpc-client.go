package main

import (
	"fmt"
	"github.com/kolo/xmlrpc"
)

func main() {
	var person_height string
	var person_gender string
	var remote_result any

	fmt.Println("Enter your height (in centimeters): ")
	fmt.Scanln(&person_height)
	fmt.Println("Enter your gender (M for male | F for female): ")
	fmt.Scanln(&person_gender)

	client, _ := xmlrpc.NewClient("http://localhost:8000/", nil)
	client.Call("calculate_ideal_weight", []interface{}{person_height, person_gender}, &remote_result)

    fmt.Println(remote_result)
}