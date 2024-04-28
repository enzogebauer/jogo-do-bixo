import random
import xmlrpc.server

class BlackJack:
    def __init__(self):
        self.client_hand = []
        self.dealer_hand = []
        self.values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'A': 1, 'J': 10, 'Q': 10, 'K': 10}
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.dig_cards = []

    def start_dig(self):
        self.dig_cards = [(value, suit) for value in self.values.keys() for suit in self.suits]

    def start_dealer_hand(self):
        for _ in range(0, 3):
            random_card = random.choice(self.dig_cards)
            self.dig_cards.remove(random_card)
            self.dealer_hand.append(random_card)

    def dealer_hand_sum(self):
        total = sum(self.values[card[0]] for card in self.dealer_hand)
        ace_count = sum(1 for card in self.dealer_hand if card[0] == 'A')

        # Trata os Ases como 11, desde que isso não faça o total ultrapassar 21
        while ace_count > 0 and total + 10 <= 21:
            total += 10
            ace_count -= 1

        return total

    def client_hand_sum(self):
        total = sum(self.values[card[0]] for card in self.client_hand)
        ace_count = sum(1 for card in self.client_hand if card[0] == 'A')

        # Trata os Ases como 11, desde que isso não faça o total ultrapassar 21
        while ace_count > 0 and total + 10 <= 21:
            total += 10
            ace_count -= 1

        return total

    def get_client_hand(self):
        return self.client_hand
    
    def client_throw_card(self):
        random_card = random.choice(self.dig_cards)
        self.dig_cards.remove(random_card)
        self.client_hand.append(random_card)
            
    def define_winner(self):
        dealer_hand_sum = self.dealer_hand_sum()
        client_hand_sum = self.client_hand_sum()

        if dealer_hand_sum > 21 and client_hand_sum <= 21:
            return 1 # Client Venceu
        elif dealer_hand_sum <= 21 and (dealer_hand_sum > client_hand_sum or client_hand_sum > 21):
            return -1 # Dealer Venceu
        elif dealer_hand_sum == client_hand_sum:
            return 0 # Empate Venceu
        else:
            return 1 # Client Venceu
    
    def get_feed(self):
        feed_string = ""
        feed_string += "Cartas cliente: {}\n".format(self.client_hand)
        feed_string += "Soma cliente: {}\n".format(self.client_hand_sum())
        feed_string += "Cartas Dealer: {}\n".format(self.dealer_hand)
        feed_string += "Soma Dealer: {}\n".format(self.dealer_hand_sum())
        
        return feed_string
    
    def get_winner(self):
        # Determina o vencedor e exibe as informações finais
        if self.define_winner() == 1:
            return "Voce Venceu!"
        elif self.define_winner() == 0:
            return "Empate!"
        elif self.define_winner() == -1:
            return "Dealer Venceu!"

server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000), allow_none=True)

print("BlackJack iniciado!")

server.register_instance(BlackJack())
server.serve_forever()
