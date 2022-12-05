import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    employee_name = input("Enter the employee name: ")
    employee_position = input("Enter the employee level (A, B, C, D): ")
    employee_salary = input("Enter the employee salary: $")
    employee_dependents = input("Enter the employee number of dependents: ")
    remote_result = proxy.employee_new_salary(employee_name, employee_position, employee_salary, employee_dependents)
    print(remote_result)
