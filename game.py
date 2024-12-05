import deal
import copy
import trick
import score
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

    def __init__(self,my_game):
        self.my_game = my_game
        # This is the actual trick where users play their cards
        self.trick = {}
        game2 = copy.deepcopy(MY_GAME)
        
        for key in game2:
            game2[key] = ""
            
            
    # If we want to debug I created a magic method to print Game objects
    def __str__(self):
        ret = ""
        for name, hand in self.my_game.items():
            ret += name + "'s cards" ": "
            for card in hand:
                ret += f"|{str(card[1])} of {card[0]}| "

            ret += ("\n")
            
        return ret
    

    
    def gameplay(self):
        self.scoreboard = {}
        # Just some stuff to see who is first, don't really need to know how it works
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
        # Haven't finished this yet but it will run until the game is "finished" (someone gets a certain score)
        
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
                    """Conditions or try except blocks can be HERE to catch any situations where a player plays a heart card accedently for example """
                
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
            print(f"\n{winner_name} wins the trick stack as they placed a(n) {highest[0]} of {highest[1]}")
            scoreboard = score.score(trick_copy, winner_name)
            if self.scoreboard == {}:
                self.scoreboard.update(scoreboard)
                print(f"Current Score ---> {scoreboard}\n")
                
            else:
                result = {name: self.scoreboard[name] + scoreboard[name] for name in self.scoreboard}
                self.scoreboard.update(result)
                print(f"Current Score ---> {result}\n")
            
    
            




# Calls everything  
game = Game(MY_GAME)
game.gameplay()