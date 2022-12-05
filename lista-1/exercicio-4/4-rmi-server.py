import Pyro5.api 

@Pyro5.api.expose
class IdealWeight(object):
    def calculate_ideal_weight(self, person_height, person_gender):
        person_height = float(person_height) / 100.0
        ideal_weight = 0.0

        if person_gender == "M":
            ideal_weight = float((72.7 * person_height) - 58.0)

        elif person_gender == "F":
            ideal_weight = float((62.1 * person_height) - 44.7)

        return "Your ideal weight is: " + "{:.2f}".format(ideal_weight) + " kg."

daemon = Pyro5.server.Daemon()  # make a Pyro daemon
ns = Pyro5.api.locate_ns()  # find the name server
uri = daemon.register(IdealWeight)  # register the greeting maker as a Pyro object
# register the object with a name in the name server
ns.register("calculate_ideal_weight", uri)

print("Ready.")
daemon.requestLoop()  # start the event loop of the server to wait for calls
