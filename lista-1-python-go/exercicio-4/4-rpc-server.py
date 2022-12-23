from xmlrpc.server import SimpleXMLRPCServer

def calculate_ideal_weight(person_height, person_gender):
    person_height = float(person_height) / 100.0
    ideal_weight = 0.0

    if person_gender == "M":
        ideal_weight = float((72.7 * person_height) - 58.0)

    elif person_gender == "F":
        ideal_weight = float((62.1 * person_height) - 44.7)

    return "Your ideal weight is: " + "{:.2f}".format(ideal_weight) + " kg."

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(calculate_ideal_weight, "calculate_ideal_weight")
server.serve_forever()