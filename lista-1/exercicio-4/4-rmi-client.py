import Pyro5.api

# use name server object lookup uri shortcut
server = Pyro5.api.Proxy("PYRONAME:calculate_ideal_weight")

person_height = input("Enter your height (in centimeters): ")
person_gender = input("Enter your gender (M for male | F for female): ")
remote_result = server.calculate_ideal_weight(person_height, person_gender)
print(remote_result)