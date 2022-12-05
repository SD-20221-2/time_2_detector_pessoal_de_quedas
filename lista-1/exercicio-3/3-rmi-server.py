import Pyro5.api 

@Pyro5.api.expose
class Grade(object):
    def grade_avg(self, grade_N1, grade_N2):
        N1 = float(grade_N1)
        N2 = float(grade_N2)
        avg = (N1 + N2)/2

        if avg >= 7:
            return "Aprovado(a)!"
        elif avg <= 3:
            return "Reprovado(a)!"
        elif avg > 3 and avg < 7:
            return avg

    def total_avg(self, grade_N3, avg):
        N3 = float(grade_N3)
        AVG = float(avg)
        calc = (N3 + AVG)/2

        if calc >= 5:
            return "Aprovado(a)!"
        else:
            return "Reprovado(a)!"

daemon = Pyro5.api.Daemon()  # make a Pyro daemon
ns = Pyro5.api.locate_ns()  # find the name server
uri = daemon.register(Grade)  # register the greeting maker as a Pyro object
# register the object with a name in the name server
ns.register("avg", uri)

print("Ready.")
daemon.requestLoop()  # start the event loop of the server to wait for calls