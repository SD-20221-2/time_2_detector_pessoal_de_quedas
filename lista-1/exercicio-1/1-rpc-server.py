from xmlrpc.server import SimpleXMLRPCServer

def employee_new_salary(employee_name, employee_position, employee_salary):
    employee_salary = float(employee_salary) # string to float
    employee_new_salary = 0

    if employee_position == "operador":
        employee_new_salary = float(employee_salary * 1.2)

    elif employee_position == "programador":
        employee_new_salary = float(employee_salary * 1.18)

    return employee_name + "'s new salary is $" + "{:.2f}".format(employee_new_salary) + "." # float to string with 2 decimal places

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(employee_new_salary, "employee_new_salary")
server.serve_forever()