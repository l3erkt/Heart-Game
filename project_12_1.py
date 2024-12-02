import random
import deck


""" 
Using the deck module I am creating a variable called deck that has all 
52 cards in them and shuffling them before I start my player class.
"""
deck = deck.deck
random.shuffle(deck)

class Player:
    
    def __init__(self, name):
        """
        Here I am initializing both name and hand to create 
        an instance of a player.
        """
        self.name = name
        self.hand = {self.name: []}
        
    
    def deal(self, cards_per_player=13):
        """
        After creating my attributes I am iterating through the first 13 
        cards by default in my deck variable and popping them and appending them 
        two my player hand.
        """
        for _ in range(cards_per_player):
            card = deck.pop()
            self.hand[self.name].append(card)

        
    
    #RETURN
    """
    Player <obj>   --->   {name : [[card], [card], [card]]}
    You can obtain the name of the obj by: <obj>.name
    or obtain the hand by <obj>.hand
    """

def table():
    """
    Here I am asking the users for each players name.
    Then I am adding the name to my Players class and creating an instance of
    that player.
    Then I deal them cards.
    And finally update my table variable that was initally an empty dictionary
    to the players hand
    
    """
    table = dict() 
    for i in range(1, 5):
        name = input(f'Player{i} name: ') 
        p = Player(name)
        p.deal()
        table.update(p.hand)        
        
    return table


def check_game_status(table):
    for name, hand in table.items():
        print(name,":")
        for card in hand:
            print(card[1],"of",card[0], end = ", ")
        print("\n")
            
    #RETURN
    """
    table = {
            bk : [[card], [card], [card]...],
            kyle : [[card], [card], [card]...],
            melat : [[card], [card], [card]...],
            hamza : [[card], [card], [card]...]
        }
    """
def find_first(table):
    fl = False
    for name, hand in table.items():
        for card in hand:
            if str(card[1]) == "2" and card[0] == "club":
                print(name, "is the first player")
                fl = True

my_game = table()
# check_game_status(my_game)
find_first(my_game)
