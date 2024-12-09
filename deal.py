# kyle
import random
import deck

# shuffling cards
deck = deck.deck
random.shuffle(deck)


class Player:
    """
    A class that distributes 13 cards to each player
    """
    
    def __init__(self, name):
        """
    Initializing attributes for instance of players for game
    
    Attributes: 
        deck : (lists in list)
            This attribute has all the cards in a standard deck of cards
            
        hands : (dict)
            this attribute creates a dictionary that has a key and value pair of...  player : []
            
            
    Args:
        players : (int)
            This args provides the numbers of players playing the game
            
    Returns:   
        players : (class)
            An obj that provides a dictionary of players hands by calling 
            .hands
            
    Side Effect:
         N/A
     
        """
    
        #instance attribute
        self.name = name
        self.hand = {self.name: []}


        
    
    def deal(self, cards_per_player=13):
        """
    This method deals the cards to each players hand
    
    Attributes: 
        N/A
            
                   
    Args:
        cards_per_player : (int)
            By default, each player should have 13 cards
            
    Returns:   
        N/A
            
    Side Effect:
        N/A
     
        """
        for _ in range(cards_per_player):
            card = deck.pop()
            self.hand[self.name].append(card)
            



def table():
    
    table = dict()
    print("--- Heart Game ---")
    for i in range(1, 5):
        name = input(f'Player{i} name: ') 
        p = Player(name)
        p.deal()
        table.update(p.hand)

    print('\n')        
        
    return table
