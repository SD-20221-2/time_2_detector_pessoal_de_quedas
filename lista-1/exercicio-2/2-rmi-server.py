import Pyro5.api

@Pyro5.api.expose
class Salary(object):
    def employee_new_salary(self, employee_name, employee_position, employee_salary):
        employee_salary = float(employee_salary) # string to float
        employee_new_salary = 0

        if employee_position == "operador":
            employee_new_salary = float(employee_salary * 1.2)

        elif employee_position == "programador":
            employee_new_salary = float(employee_salary * 1.18)

        return employee_name + "'s new salary is $" + "{:.2f}".format(employee_new_salary) + "." # float to string with 2 decimal places

daemon = Pyro5.server.Daemon() # make a Pyro daemon
ns = Pyro5.api.locate_ns() # find the name server
uri = daemon.register(Salary) # register the greeting maker as a Pyro object
ns.register("new_salary", uri) # register the object with a name in the name server

print("Ready.")
daemon.requestLoop() # start the event loop of the server to wait for calls