import Pyro5.api

# use name server object lookup uri shortcut
server = Pyro5.api.Proxy("PYRONAME:age_majority")

person_name = input("Enter your name: ")
person_gender = input("Enter your gender (M for male | F for female): ")
person_age = input("Enter your age: ")
remote_result = server.age_majority(person_name, person_gender, person_age)
print(remote_result)