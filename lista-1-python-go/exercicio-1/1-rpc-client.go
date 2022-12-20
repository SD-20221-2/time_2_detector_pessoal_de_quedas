package main

import (
	"fmt"
	"github.com/kolo/xmlrpc"
)

func main() {
	var employee_name string
	var employee_position string
	var employee_salary string
	var result string

	fmt.Println("Enter the employee name: ")
	fmt.Scanln(&employee_name)
	fmt.Println("Enter the employee position: ")
	fmt.Scanln(&employee_position)
	fmt.Println("Enter the employee salary: $")
	fmt.Scanln(&employee_salary)

	client, _ := xmlrpc.NewClient("http://localhost:8000/", nil)
	client.Call("employee_new_salary", []interface{}{employee_name, employee_position, employee_salary}, &result)
	fmt.Printf(result) 
}