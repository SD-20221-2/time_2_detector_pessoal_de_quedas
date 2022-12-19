from xmlrpc.server import SimpleXMLRPCServer

def can_retire(name, age, service_time):

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

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(can_retire, "can_retire")
server.serve_forever()