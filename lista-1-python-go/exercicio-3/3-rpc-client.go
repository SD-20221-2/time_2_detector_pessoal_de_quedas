package main

import (
	"fmt"
	"github.com/kolo/xmlrpc"
	"reflect"
)

func main() {
	var grade_N1 string
	var grade_N2 string
	var grade_N3 string
	var remote_result any

	fmt.Println("Enter the first grade: ")
	fmt.Scanln(&grade_N1)
	fmt.Println("Enter the second grade:")
	fmt.Scanln(&grade_N2)

	client, _ := xmlrpc.NewClient("http://localhost:8000/", nil)
	client.Call("grade_avg", []interface{}{grade_N1, grade_N2}, &remote_result)
	varType := reflect.TypeOf(remote_result).String()

	if string(varType) == "float64" {
		var result string
		fmt.Println("Need to enter the third grade!")
		fmt.Println("Enter the third grade: ")
		fmt.Scanln(&grade_N3)
		client.Call("total_avg", []interface{}{grade_N3, remote_result}, &result)
		fmt.Println(result)
	} else {
		fmt.Println(remote_result)
	}
}