//go get github.com/kolo/xmlrpc

package main

import (
	"fmt"
	"github.com/kolo/xmlrpc"
)

func main() {
	var employee_name string
	var employee_position string
	var employee_salary string
	var employee_dependents string
	var result string

	fmt.Println("Enter your name: ")
	fmt.Scanln(&employee_name)
	fmt.Println("Enter the employee level (A, B, C, D): ")
	fmt.Scanln(&employee_position)
	fmt.Println("Enter the employee salary: $")
	fmt.Scanln(&employee_salary)
	fmt.Println("Enter the employee number of dependents: ")
	fmt.Scanln(&employee_dependents)

	client, _ := xmlrpc.NewClient("http://localhost:8000/", nil)
	client.Call("employee_new_salary", []interface{}{employee_name, employee_position, employee_salary, employee_dependents}, &result)
	fmt.Printf(result) 
}
