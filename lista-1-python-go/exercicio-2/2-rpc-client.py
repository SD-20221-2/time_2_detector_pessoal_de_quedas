import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    person_name = input("Enter your name: ")
    person_gender = input("Enter your gender (M for male | F for female): ")
    person_age = input("Enter your age: ")
    remote_result = proxy.age_majority(person_gender, person_age)
    print(remote_result)