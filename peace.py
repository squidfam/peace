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
    print(f"Player 1 played {player1_hand[0]} and Player 2 played {player2_hand[0]}")
    temp_deck = [player1_hand.pop(0),player2_hand.pop(0)]

    if battle_result == 1:
        print("Player 1 beat Player 2 and took their cards")
        return player1_hand, player2_hand
    elif battle_result == 2:
        print("Player 2 beat Player 1 and took their cards")
        return player1_hand,player2_hand
    else:
        print("Looks like we're going to war")
        player1_hand,player2_hand = peace(player1_hand,player2_hand)
        return player1_hand,player2_hand

def peace(player1_hand, player2_hand):
    temp_deck = []

    while len(player1_hand) > 3 and len(player2_hand)> 3:

        temp_deck +=  [player1_hand.pop(0) for _ in range(3)]
        temp_deck += [player2_hand.pop(0) for _ in range(3)]
        print("Both players have given up three cards")
        print(f"Player 1 brings {player1_hand[0]} and Player 2 brings {player2_hand} to war")
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
        temp_deck += [player1_hand.pop(0) for _ in range(len(player1_hand)-1)]
        temp_deck += [player2_hand.pop(0) for _ in range(len(player2_hand)-1)]
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
            return player1_hand,player2_hand
    else:
        return player1_hand,player2_hand

        
def play_game(deck1,deck2):
    while len(deck1) > 0 and len(deck2) > 0:
        deck1,deck2 = play_round(deck1,deck2)
    if len(deck1) == 0:
        print("Player 2 wins!")
    elif len(deck2) == 0:
        print("Player 1 wins")
    else:
        print("It's a tie!")

play_game(deck1,deck2)
