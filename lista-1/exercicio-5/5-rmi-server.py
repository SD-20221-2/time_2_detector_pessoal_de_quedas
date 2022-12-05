import Pyro5.api

@Pyro5.api.expose
class SwimmerCategory(object):
    def verify_swimmer_category(self, swimmer_age):
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

daemon = Pyro5.server.Daemon()  # make a Pyro daemon
ns = Pyro5.api.locate_ns()  # find the name server
uri = daemon.register(SwimmerCategory)  # register the greeting maker as a Pyro object
# register the object with a name in the name server
ns.register("verify_swimmer_category", uri)

print("Ready.")
daemon.requestLoop()  # start the event loop of the server to wait for calls
