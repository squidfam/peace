import random

ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")
deck =  [(suit,rank) for suit in suits for rank in ranks]
random.shuffle(deck)
deck1 = deck[:len(deck)//2]
deck2 = deck[len(deck)//2:]

def card_comparison(p1_card, p2_card):

    if ranks.index(p1_card[1]) > ranks.index(p2_card[1]):
        return 1
    elif ranks.index(p1_card[1]) < ranks.index(p2_card[1]):
        return 2
    else:
        return 0

def play_round(player1_hand, player2_hand):

    battle_result = card_comparison(player1_hand[0],player2_hand[0])

    if battle_result == 1:
        temp_deck = [player1_hand.pop(0),player2_hand.pop(0)]
        player1_hand.extend(temp_deck)
        return player1_hand, player2_hand
    elif battle_result == 2:
        temp_deck = [player1_hand.pop(0),player2_hand.pop(0)]
        player2_hand.extend(temp_deck)
        return player1_hand,player2_hand
    else:
        player1_hand,player2_hand = peace(player1_hand,player2_hand)
        return player1_hand,player2_hand

def peace(player1_hand, player2_hand):
    temp_deck = []

    while len(player1_hand) > 3 and len(player2_hand)> 3:

        temp_deck.extend(player1_hand[:3])
        temp_deck.extend(player2_hand[:3])
        del player1_hand[:3]
        del player2_hand[:3]
        peace_result = card_comparison(player1_hand[0],player2_hand[0])
        temp_deck.append(player1_hand.pop(0))
        temp_deck.append(player2_hand.pop(0))

        if peace_result == 1:
            player1_hand.extend(temp_deck)
            return player1_hand,player2_hand
        elif peace_result == 2:
            player2_hand.extend(temp_deck)
            return player1_hand,player2_hand

    if len(player1_hand) > 0 and len(player2_hand) > 0:
        temp_deck.extend(player1_hand[:-1])
        temp_deck.extend(player2_hand[:-1])
        del player1_hand[:-1]
        del player2_hand[:-1]
        peace_result = card_comparison(player1_hand[0],player2_hand[0])
        temp_deck.append(player1_hand.pop(0))
        temp_deck.append(player2_hand.pop(0))


        if peace_result == 1:
            player1_hand.extend(temp_deck)
            return player1_hand,player2_hand
        elif peace_result == 2:
            player2_hand.extend(temp_deck)
            return player1_hand,player2_hand
    else:
        if len(player1_hand) == 0 and player2_hand != 0:
            return "Player 2 wins!"
        elif len(player2_hand) == 0 and player1_hand != 0:
            return "Player 1 wins!"
        else:
            return "It's a tie!"

        
def play_game(deck1,deck2):
    while len(deck1) > 0 and len(deck2) > 0 and deck1 != "Player 1 wins!" and deck1 != "Player 2 wins!" and deck1 != "It's a tie!":
        deck1,deck2 = play_round(deck1,deck2)
        print(deck1,deck2)
    if deck1 == "it's a tie!" or deck1 == "Player 2 wins!" or deck1 == "Player 1 wins!":
        print(deck1)
    elif len(deck1) == 0:
        print("Player 2 wins!")
    else:
        print("Player 1 wins")

play_game(deck1,deck2)
