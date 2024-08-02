from itertools import cycle
from card_dealer import array_of_cards 
from hand_sorter import values_val

def create_player_matrix(m, n, values):
    value_cycle = cycle(values)
    return [[next(value_cycle) for _ in range(n)] for _ in range(m)]

def deal_hands(cards, num_players):
    """Deals cards to players and returns a list of hands."""
    hands = create_player_matrix(num_players, 2, cards)
    for i, hand in enumerate(hands):
        print(f"Hand {i+1}: {hand}")
    return hands

def runout_creator(cards, num_players):
    """Creates a list of community cards."""
    return cards[num_players * 2:]

def super_hand_creator(hands, runout):
    for i, hand in enumerate(hands):
        for x in range (len(runout)):
            (hands[i]).append(runout[x])
        #print(f"Hand {i+1}: {hands[i]}")
        hands[i]= values_val(hands[i])
        print(f"sorted hand {i+1}: {hands[i]}")



def main():
    num_players = int(input("How many players? "))
    num_cards = num_players * 2 + 5
    cards = array_of_cards(num_cards)

    hands = deal_hands(cards, num_players)
    runout = runout_creator(cards, num_players)
    super_hand_creator(hands,runout)
    print("Runout:", runout)
    

if __name__ == "__main__":
    main()
