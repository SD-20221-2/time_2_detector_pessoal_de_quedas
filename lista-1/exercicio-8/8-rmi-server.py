import Pyro5.api

@Pyro5.api.expose
class Credit(object):
    def get_credit(self, average_balance):
        average_balance = float(average_balance) # string to float
        credit = 0 # default condition (average_balance >= 0 and average_balance <= 200)

        if average_balance >= 201 and average_balance <= 400:
            credit = float(average_balance * 0.2)

        elif average_balance >= 401 and average_balance <= 600:
            credit = float(average_balance * 0.3)

        elif average_balance > 601:
            credit = float(average_balance * 0.4)

        return "Average balance: $" + "{:.2f}".format(average_balance) + " | Credit: $" + "{:.2f}".format(credit) + "." # floats to string with 2 decimal places

daemon = Pyro5.server.Daemon() # make a Pyro daemon
ns = Pyro5.api.locate_ns() # find the name server
uri = daemon.register(Credit) # register Credit as a Pyro object
ns.register("Credit", uri) # register the object with a name in the name server

print("Ready.")
daemon.requestLoop() # start the event loop of the server to wait for calls