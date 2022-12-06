import Pyro5.api

@Pyro5.api.expose
class Retire(object):
    def employee_new_salary(self, name, age, service_time):
        
        age = float(age)
        service_time = float(service_time)

        can_retire = 0

        if age >= 65: 
            can_retire = 1
        elif service_time >= 30:
            can_retire = 1
        elif age >= 60 and service_time >= 25:
            can_retire = 1
        else:
            can_retire = 0

        if can_retire == 1: 
            return "Employee: " + str(name) + " can retire"
        else:
            return "Employee: " + str(name) + " cannot retire yet"

daemon = Pyro5.server.Daemon() # make a Pyro daemon
ns = Pyro5.api.locate_ns() # find the name server
uri = daemon.register(Retire) # register Retire as a Pyro object
ns.register("retire", uri) # register the object with a name in the name server

print("Ready.")
daemon.requestLoop() # start the event loop of the server to wait for calls
