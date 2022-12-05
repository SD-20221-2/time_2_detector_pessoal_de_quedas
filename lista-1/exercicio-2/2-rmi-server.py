import Pyro5.api

@Pyro5.api.expose
class Person(object):
    def age_majority(self, person_name, person_gender, person_age):
        if person_gender == "M" and float(person_age) >= 18:
            return "You've come of age!"

        elif person_gender == "M" and float(person_age) < 18:
            return "You didn't come of age. Males don't come of age until they are 18!"

        if person_gender == "F" and float(person_age) >= 21:
            return "You've come of age!"

        elif person_gender == "F" and float(person_age) < 21:
            return "You didn't come of age. Females don't come of age until they are 21!"


daemon = Pyro5.api.Daemon()  # make a Pyro daemon
ns = Pyro5.api.locate_ns()  # find the name server
uri = daemon.register(Person)  # register the greeting maker as a Pyro object
# register the object with a name in the name server
ns.register("age_majority", uri)

print("Ready.")
daemon.requestLoop()  # start the event loop of the server to wait for calls
