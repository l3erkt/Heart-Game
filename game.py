import deal
import copy
import trick


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
                print(f"Current trick --> {self.trick}")
                # Asks for what suit/number they want to play
                
                suit_choice = input(f"{com[i]}, What suit would you like to play? ")
                num_choice = input("What number of that suit would you like to play? ")
                """Conditions or try except blocks can be HERE to catch any situations where a player plays a heart card accedently for example """
                
                if num_choice.isdigit():
                    num_choice = int(num_choice)
                    
                paired = [suit_choice,num_choice]
                self.trick[com[i]] = paired        
                self.my_game[com[i]].remove(paired)
                print('\n')
                
        
            """# TRICK FUNCTION HERE to evaluate who gets the trick stack...
            trick.trick(self.my_game, self.trick)"""
            




# Calls everything  
game = Game(MY_GAME)
game.gameplay()