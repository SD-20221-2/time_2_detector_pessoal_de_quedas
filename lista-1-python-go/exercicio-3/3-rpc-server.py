from xmlrpc.server import SimpleXMLRPCServer

def grade_avg(grade_N1, grade_N2):
    N1 = float(grade_N1)
    N2 = float(grade_N2)
    avg = (N1 + N2)/2

    if avg >= 7:
        return "Aprovado(a)!"
    elif avg <= 3:
        return "Reprovado(a)!"
    elif avg > 3 and avg < 7:
        return avg

def total_avg(grade_N3, avg):
    N3 = float(grade_N3)
    AVG = float(avg)
    calc = (N3 + AVG)/2

    if calc >= 5:
        return "Aprovado(a)!"
    else:
        return "Reprovado(a)!"

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(grade_avg, "grade_avg")
server.register_function(total_avg, "total_avg")
server.serve_forever()