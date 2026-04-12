import time
import random
suits = ['Clubs', 'Diamonds', 'Spades', 'Hearts']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.is_face = False

        if self.rank in ['Jack', 'Queen', 'King']:
            self.is_face = True

    def __repr__(self):
        return f'{self.rank} of {self.suit}'
            
class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0

    def deal(self, deck, num):
        for i in range(0, num):
            if deck:
                self.cards.append(deck.pop(0))

    def __repr__(self):
        result = ""
        for i in range(0, len(self.cards)):
            result += f'{repr(self.cards[i])}\n'
        result += f'\nCurrent value: {self.value}'
        return result
    
    def calc_hand_value(self):
        self.value = 0
        for card in self.cards:
            if card.rank == 'Ace':
                self.value += 11
                if self.value > 21:
                    self.value -= 10
            elif card.is_face:
                self.value += 10
            else:
                self.value += int(card.rank)

class Player():
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

def get_game_state(player):
    player.hand.calc_hand_value()
    print(player.hand)
    choice = input("\nWould you like to Hit or Stand?\n")
    return choice.lower()

def main():
    deck = []
    player = Player('Player 1', Hand())
    dealer = Player('Dealer', Hand())
    players = [player, dealer]

    for suit in suits:
        for rank in ranks:
            deck.append(Card(rank, suit))
    
    random.shuffle(deck)
    
    for p in players:
        p.hand.deal(deck, 2)

    while(player.hand.value < 21):
        choice = get_game_state(player)
        if choice == 'hit':
            player.hand.deal(deck, 1)
            continue
        elif choice == 'stand':
            break
        else:
            print("Please enter either 'hit' or 'stand'\n")
            time.sleep(1)

    while(dealer.hand.value < 21):
        if dealer.hand.value < 14:
            dealer.hand.deal(deck, 1)
            dealer.hand.calc_hand_value()
            continue
        if dealer.hand.value >= 14:
            break
    
    if player.hand.value > 21:
        player_result = "BUST"
    else:
        player_result = player.hand.value
    
    if dealer.hand.value > 21:
        dealer_result = "BUST"
    else:
        dealer_result = dealer.hand.value
    print(dealer.hand)
    time.sleep(1)
    print(f'Player\'s score: {player_result}\nDealer\'s score: {dealer_result}')
    if dealer_result == player_result:
        end_result = "tie"
    elif dealer_result == 'BUST' and player_result != 'BUST':
        end_result = "win"
    elif dealer_result < player_result:
        end_result = "win"
    else:
        end_result = "lose"

    if end_result == "win":
        print("Congratulations! You won!")
    elif end_result == "tie":
        print("It's a tie! better luck next time.")
    else:
        print("Sorry, you lost.  Better luck next time!")

main()

    


