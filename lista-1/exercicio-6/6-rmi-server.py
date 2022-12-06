import Pyro5.api

@Pyro5.api.expose
class Salary(object):
    def employee_new_salary(self, employee_name, employee_position, employee_salary, employee_dependents):
        employee_salary = float(employee_salary) # string to float
       
        employee_salary = float(employee_salary)
        employee_dependents = float(employee_dependents)

        percentage_discount = 0

        if employee_position == "A" and employee_dependents >= 1:
            percentage_discount = 8
        elif employee_position == "A" and employee_dependents >= 0:
            percentage_discount = 3

        elif employee_position == "B" and employee_dependents >= 1:
            percentage_discount = 10
        elif employee_position == "A" and employee_dependents >= 0:
            percentage_discount = 5

        elif employee_position == "C" and employee_dependents >= 1:
            percentage_discount = 15
        elif employee_position == "C" and employee_dependents >= 0:
            percentage_discount = 8

        elif employee_position == "D" and employee_dependents >= 1:
            percentage_discount = 17
        elif employee_position == "D" and employee_dependents >= 0:
            percentage_discount = 10

        employee_new_salary = employee_salary - ((employee_salary*percentage_discount)/100)

        return employee_name + "'s new salary is $" + "{:.2f}".format(employee_new_salary) + "." # float to string with 2 decimal places

daemon = Pyro5.server.Daemon() # make a Pyro daemon
ns = Pyro5.api.locate_ns() # find the name server
uri = daemon.register(Salary) # register Salary as a Pyro object
ns.register("new_salary", uri) # register the object with a name in the name server

print("Ready.")
daemon.requestLoop() # start the event loop of the server to wait for calls