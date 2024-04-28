import xmlrpc.client

# Conecta-se ao servidor RPC
BlackJack = xmlrpc.client.ServerProxy("http://localhost:8000")

# Inicia o jogo
BlackJack.start_dig()
BlackJack.start_dealer_hand()

choose = " "

while choose.upper() != "STAND":
    choose = input("Choose a option HIT or STAND: ")

    while choose.upper() not in ["HIT", "STAND"]:
        if choose.upper() == "HIT":
            BlackJack.client_throw_card()

    print("Suas cartas atuais:", BlackJack.get_client_hand())
    print("Soma atual de cartas:", BlackJack.client_hand_sum())

print(BlackJack.get_feed())
print(BlackJack.get_winner())
