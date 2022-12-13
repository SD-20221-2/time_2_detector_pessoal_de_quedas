from xmlrpc.server import SimpleXMLRPCServer

def age_majority(person_name, person_gender, person_age):
    if person_gender == "M" and float(person_age) >= 18:
        return person_name + " come of age!"
    elif person_gender == "M" and float(person_age) < 18:
        return person_name + " didn't come of age. Males don't come of age until they are 18!"

    if person_gender == "F" and float(person_age) >= 21:
        return person_name + " come of age!"
    elif person_gender == "F" and float(person_age) < 21:
        return person_name + " didn't come of age. Females don't come of age until they are 21!"

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(age_majority, "age_majority")
server.serve_forever()