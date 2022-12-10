import Pyro5.api

server_card_1 = Pyro5.api.Proxy("PYRONAME:Playing_card") # use name server object lookup uri shortcut
card_1_value = input("Enter the card value (number/letter): ")
card_1_suit = input("Enter the card suit (symbol): ")
server_card_1.initialize(card_1_value, card_1_suit)
print(server_card_1.return_str())

server_card_2 = Pyro5.api.Proxy("PYRONAME:Playing_card") # use name server object lookup uri shortcut
card_2_value = input("Enter the card value (number/letter): ")
card_2_suit = input("Enter the card suit (symbol): ")
server_card_2.initialize(card_2_value, card_2_suit)
print(server_card_2.return_str())

server_card_3 = Pyro5.api.Proxy("PYRONAME:Playing_card") # use name server object lookup uri shortcut
card_3_value = input("Enter the card value (number/letter): ")
card_3_suit = input("Enter the card suit (symbol): ")
server_card_3.initialize(card_3_value, card_3_suit)
print(server_card_3.return_str())