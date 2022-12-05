import Pyro5.api

# use name server object lookup uri shortcut
avg = Pyro5.api.Proxy("PYRONAME:avg")

grade_N1 = input("Enter the first grade: ")
grade_N2 = input("Enter the second grade: ")

remote_result = avg.grade_avg(grade_N1, grade_N2)

if type(remote_result) is float:
    print("Need to enter the third grade!")
    grade_N3 = input("Enter the third grade: ")
    result = avg.total_avg(grade_N3, remote_result)
    print(result)
else:
    print(remote_result)
