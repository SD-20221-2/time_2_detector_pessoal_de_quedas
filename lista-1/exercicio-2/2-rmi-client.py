import Pyro5.api

server = Pyro5.api.Proxy("PYRONAME:new_salary") # use name server object lookup uri shortcut

employee_name = input("Enter the employee name: ")
employee_position = input("Enter the employee position: ")
employee_salary = input("Enter the employee salary: $")
remote_result = server.employee_new_salary(employee_name, employee_position, employee_salary)
print(remote_result)