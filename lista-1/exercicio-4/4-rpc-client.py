import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    person_height = input("Enter your height (in centimeters): ")
    person_gender = input("Enter your gender (M for male | F for female): ")
    remote_result = proxy.calculate_ideal_weight(person_height, person_gender)
    print(remote_result)