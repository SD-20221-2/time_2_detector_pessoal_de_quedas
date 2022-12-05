import Pyro5.api

server = Pyro5.api.Proxy("PYRONAME:verify_swimmer_category") # use name server object lookup uri shortcut

swimmer_age = input("Enter your age: ")
remote_result = server.verify_swimmer_category(swimmer_age)
print(remote_result)