import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    name = input("Enter the employee name: ")
    age = input("Enter your age: ")
    service_time = input("Enter your service time: ")
    remote_result = proxy.employee_new_salary(name, age, service_time)
    print(remote_result)