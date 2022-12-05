import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    grade_N1 = input("Enter the first grade: ")
    grade_N2 = input("Enter the second grade: ")

    remote_result = (proxy.grade_avg(grade_N1, grade_N2))

    if type(remote_result) is float: 
        print("Need to enter the third grade!")
        grade_N3 = input("Enter the third grade: ")
        result = proxy.total_avg(grade_N3, remote_result)
        print(result)
    else:
        print(remote_result)
