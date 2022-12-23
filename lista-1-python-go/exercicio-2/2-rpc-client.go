package main

import (
	"fmt"
	"github.com/kolo/xmlrpc"
)

func main() {
	var person_name string
	var person_gender string
	var person_age string
	var result string

	fmt.Println("Enter your name: ")
	fmt.Scanln(&person_name)
	fmt.Println("Enter your gender (M for male | F for female): ")
	fmt.Scanln(&person_gender)
	fmt.Println("Enter your age: ")
	fmt.Scanln(&person_age)

	client, _ := xmlrpc.NewClient("http://localhost:8000/", nil)
	client.Call("age_majority", []interface{}{person_name, person_gender, person_age}, &result)
	fmt.Printf(result) 
}
