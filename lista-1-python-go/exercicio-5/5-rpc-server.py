from xmlrpc.server import SimpleXMLRPCServer

def verify_swimmer_category(swimmer_age):
    swimmer_age = int(swimmer_age)
    swimmer_category = ""

    if swimmer_age >= 18:
        swimmer_category = "Adults"

    elif swimmer_age >= 14:
        swimmer_category = "Youth B"

    elif swimmer_age >= 11:
        swimmer_category = "Youth A"

    elif swimmer_age >= 8:
        swimmer_category = "Children B"

    elif swimmer_age >= 5:
        swimmer_category = "Children A"

    else:
        swimmer_category = "None"

    return "Your category is: " + swimmer_category + "."

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(verify_swimmer_category, "verify_swimmer_category")
server.serve_forever()