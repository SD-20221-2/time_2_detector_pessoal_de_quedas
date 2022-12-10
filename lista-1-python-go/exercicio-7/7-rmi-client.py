import Pyro5.api

server = Pyro5.api.Proxy("PYRONAME:retire") # use name server object lookup uri shortcut

name = input("Enter the employee name: ")
age = input("Enter your age: ")
service_time = input("Enter your service time: ")
remote_result = server.employee_new_salary(name, age, service_time)
print(remote_result)
