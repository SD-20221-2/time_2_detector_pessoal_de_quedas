import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    employee_name = input("Enter the employee name: ")
    employee_position = input("Enter the employee position: ")
    employee_salary = input("Enter the employee salary: $")
    remote_result = proxy.employee_new_salary(employee_name, employee_position, employee_salary)
    print(remote_result)