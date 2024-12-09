import deal
import copy
import trick
import score
import visual
import validation


MY_GAME = deal.table()


def current_player(table, round = 1): 
    """ 
    What it does: 
        Identifies the current player of the game 

    Args: 
        round: int - the current round of the game 
    
    Returns: 
        The current player whose turn it is
    """ 
        
    played = [] 
    round = 1 
    if round == 1 and len(played) == 0:
        for name, hand in table.items(): 
            for card in hand: 
                if card[0] == 'club' and card[1] == 2: 
                    played.append(name)
                    return name 
    elif round >= 1: 
        for name in table.keys(): 
            if name not in played: 
                played.append(name) 
                return name 
            
    if len(played) == len(table.items()):
        played.clear() 
        round += 1
    
    return None

class Game:
    """
    Creates Game class
    Attributes: __init__(),__str()__,gameplay(), convert_cards()
    Side effects: Creates __init__(),__str()__,gameplay(), convert_cards() methods. Plays the game
    Returns: val_converted in convert_cards
    """
    def __init__(self,my_game):
        """
        Author: Kyle Won
        Description: Method that initializes Game object
        Args: self,my_game
        Side effects: creates a deep copy of the my_game object, creates self.trick
        Returns: None
        Raises: ValueError if invalid number, raises TypeError if the number is the wrong data type
        """
        self.my_game = my_game
        # This is the actual trick where users play their cards
        self.trick = {}
        game2 = copy.deepcopy(MY_GAME)
        
        for key in game2:
            game2[key] = ""
            
            
    # If we want to debug I created a magic method to print Game objects
    def __str__(self):
        """
        Author: Kyle Won
        Description: Allows for a informal representation of the my_game data type
        Args: self
        Side effects: Prints cards in a player's hand
        Returns: ret: A string that contains a player's hand information
        """
        ret = ""
        for name, hand in self.my_game.items():
            ret += name + "'s cards" ": "
            for card in hand:
                ret += f"|{str(card[1])} of {card[0]}| "

            ret += ("\n\n")
            
        return ret
    

    
    def gameplay(self):
        """
        Author: Kyle Won
        Description: Contains the game's logic (for the most part)
        Args: self
        Side effects: Will print who wins, error messages for wrong card placement, and will take input from user. Will also take 
        also convert letter cards such as J,Q,K,A.
        Returns: None
        """
        self.scoreboard = {}
        # Finds who is first by searching each hand to see who has the 2 of clubs
        first_player = current_player(self.my_game)
        print(f"The first player is: {first_player}")
        unordered = list(self.my_game.keys())
        index_first = unordered.index(first_player)
        rem = unordered[index_first:]
        unordered = unordered[:index_first]
        com = rem + unordered
        for i in range(len(com)):
            self.trick[com[i]] = ""
        print(com)
        print("\n")
        finished = False
        
        while finished == False:
            
            self.trick = {}
            # This will count the turns of 4 players
            
            print(str(self))
            
        
            for i in range(4):
                # Asks for what suit/number they want to play
                valid_choice = False  # Hamza changes: Added a flag to ensure valid card choices
                while not valid_choice:  # Hamza changes: Loop to enforce valid card choice
                    suit_choice = input(f"{com[i]}, What suit would you like to play? ")
                    num_choice = input("What number of that suit would you like to play? ")
                
                    if num_choice.isdigit():
                        num_choice = int(num_choice)
                    
                    card_choice = [suit_choice, num_choice]
                    
                    if card_choice in self.my_game[com[i]]:  # Hamza changes: Ensure the card is in the player's hand
                        valid_choice = validation.validate_card_choice(
                            com[i], card_choice, self.trick, self.my_game[com[i]]
                        )  # Hamza changes: Validate the card using the custom function
                        if valid_choice:
                            self.trick[com[i]] = card_choice
                            self.my_game[com[i]].remove(card_choice)
                            print(f"\nCurrent trick --> {self.trick}\n")
                        else:
                            print(f"Invalid card choice. Try again.")  # Hamza changes: Notify player of invalid choice
                    else:
                        print(f"Card {card_choice} is not in your hand. Try again.")  # Hamza changes: Check card ownership
                
                 
            trick_copy = copy.deepcopy(self.trick)
            highest = ["", 0]
            winner_name = ""
            def convert_cards(card):
                """
                Author: Kyle Won
                Description: Helper function that converts J,Q,K,A to numbers, ranking in that order
                Args: card: a card's number 
                Side effects: Will convert a letter to a number then assign val_converted to it
                Returns: val_converted: The converted value
                """
                if  card == "A":
                    val_converted = 14
                elif  card == "K":
                    val_converted = 13
                elif  card == "Q":
                    val_converted = 12
                elif  card == "J":
                    val_converted = 11
                else:
                    val_converted = int(card)
                
                return val_converted
                    
            for key,value in trick_copy.items():
                val_converted = convert_cards(value[1])
                high_convert = convert_cards(highest[1])
                

                if high_convert < val_converted:
                    highest = value
                    winner_name = key
                        
            # my implemnentation of the scroing function            
            print(f"\n{winner_name} takes the trick stack as they placed a(n) {highest[0]} of {highest[1]}")
            scoreboard = score.score(trick_copy, self.my_game, winner_name)
            if self.scoreboard == {}:
                self.scoreboard.update(scoreboard)
                print(f"Current Score ---> {scoreboard}\n")
                
            else:
                result = {name: self.scoreboard[name] + scoreboard[name] for name in self.scoreboard}
                self.scoreboard.update(result)
                print(f"Current Score ---> {result}\n")
            
            
            
            if score.done(self.scoreboard) == True:
                finished = True
                winner = score.winner(self.scoreboard)
                visual.bar_graph(self.scoreboard)
                print(f"WOW WHAT A GAME, THE WINNER IS {winner[0]} and their score was {winner[1]}.")          
    
            


# Calls everything  
game = Game(MY_GAME)
game.gameplay()