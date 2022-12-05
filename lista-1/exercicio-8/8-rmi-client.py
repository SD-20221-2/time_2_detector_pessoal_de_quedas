import Pyro5.api

server = Pyro5.api.Proxy("PYRONAME:Credit") # use name server object lookup uri shortcut

average_balance = input("Enter last year's average balance: $")
remote_result = server.get_credit(average_balance)
print(remote_result)