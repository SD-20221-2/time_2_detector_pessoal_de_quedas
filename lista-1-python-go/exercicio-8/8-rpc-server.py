from xmlrpc.server import SimpleXMLRPCServer

def credit(average_balance):
    average_balance = float(average_balance) # string to float
    credit = 0 # default condition (average_balance >= 0 and average_balance <= 200)

    if average_balance >= 201 and average_balance <= 400:
        credit = float(average_balance * 0.2)

    elif average_balance >= 401 and average_balance <= 600:
        credit = float(average_balance * 0.3)

    elif average_balance > 601:
        credit = float(average_balance * 0.4)

    return "Average balance: $" + "{:.2f}".format(average_balance) + " | Credit: $" + "{:.2f}".format(credit) + "." # floats to string with 2 decimal places

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(credit, "credit")
server.serve_forever()