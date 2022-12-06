import Pyro5.api

@Pyro5.api.expose
class Playing_card(object):
    def initialize(self, card_value, card_suit):
        self.card_value = card_value
        self.card_suit = card_suit

    def return_str(self):
        card_value_str = ""
        card_suit_str = ""
        card_value_symbol = ""
        card_suit_unicode = ""

        if self.card_suit == "1":
            card_suit_str = "Diamonds"
            card_suit_unicode = "\u2666"

        elif self.card_suit == "2":
            card_suit_str = "Clubs"
            card_suit_unicode = "\u2663"

        elif self.card_suit == "3":
            card_suit_str = "Hearts"
            card_suit_unicode = "\u2665"

        elif self.card_suit == "4":
            card_suit_str = "Spades"
            card_suit_unicode = "\u2660"
    
        if self.card_value == "1":
            card_value_str = "Ace"
            card_value_symbol = "A"

        elif self.card_value == "2":
            card_value_str = "Two"
            card_value_symbol = "2"

        elif self.card_value == "3":
            card_value_str = "Three"
            card_value_symbol = "3"

        elif self.card_value == "4":
            card_value_str = "Four"
            card_value_symbol = "4"

        elif self.card_value == "5":
            card_value_str = "Five"
            card_value_symbol = "5"

        elif self.card_value == "6":
            card_value_str = "Six"
            card_value_symbol = "6"

        elif self.card_value == "7":
            card_value_str = "Seven"
            card_value_symbol = "7"

        elif self.card_value == "8":
            card_value_str = "Eight"
            card_value_symbol = "8"

        elif self.card_value == "9":
            card_value_str = "Nine"
            card_value_symbol = "9"

        elif self.card_value == "10":
            card_value_str = "Ten"
            card_value_symbol = "10"

        elif self.card_value == "11":
            card_value_str = "Jack"
            card_value_symbol = "J"

        elif self.card_value == "12":
            card_value_str = "Queen"
            card_value_symbol = "Q"

        elif self.card_value == "13":
            card_value_str = "King"
            card_value_symbol = "K"

        return card_value_str + " Of " + card_suit_str + ". (" + card_suit_unicode + " " + card_value_symbol + ")"
        
daemon = Pyro5.server.Daemon() # make a Pyro daemon
ns = Pyro5.api.locate_ns() # find the name server
uri = daemon.register(Playing_card) # register Playing_card as a Pyro object
ns.register("Playing_card", uri) # register the object with a name in the name server
print("Ready.")
daemon.requestLoop() # start the event loop of the server to wait for calls