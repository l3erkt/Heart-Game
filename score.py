"""
 *** IMPORTANT RULES ***
- player with lowest points wins
- A player that gets to 100 points first will stop the game and evaluate the winner.
- Each heart card is 1pt.
- The queen of spade (KILLER QUEEN) is worth 13 pt.
"""



def done(scoreboard):
    """
    Checking whether if a player has gotten to the certain amount of points to end the game
         
    Args:
        scoreboard : (dict)
            An instance of the current scoreboard based on the cycle of the game
            
    Returns:   
        done : (bool)
            Returns True if a player playing has reached 50 pts 
            
                  
                  
    Side Effect:
        N/A 
    """
    done = False
    for _, score in scoreboard.items():
        
        if score >= 50: # YOU CAN CHANGE THIS VALUE TO END THE GAME QUICKER... MAYBE TRY 10
            done = True
            
    return done




def winner(scoreboard):
    """
    Depending on all the current players, finds which one has won the game.
         
    Args:
        scoreboard : (dict)
            An instance of the current scoreboard based on the cycle of the game.
            
    Returns:   
        name, score : (tuple)
            Returns the name and score of the winner of the game.
             
                  
    Side Effect:
        N/A 
    """
    
    sb = [[name, score] for name, score in scoreboard.items()]
    name, score = sorted(sb, key=lambda plyr: plyr[1])[0]
    return name, score





def shootmoon(plyr, sb):
    """
    A players that has all 'heart' cards and the 'Q' of 'spade' in their hand.
    
    This function basically takes in the scoreboard for the game and check whether any player meets the condition.
        - Player hand MUST have a 'Q' of 'spade'
        - Player hand MUST have ALL 'heart' cards
    
               
    Args:
        plyr : (str)
            the name of the player that met the requirement of shootthemoon
    
        sb : (dict)
            This container contains each players name (str) as the key and hand (lists in list) as a value
            
    Returns:   
        sb : (dict)
            A key value pair of the players name and the score that have with their hand.
                  
                  
    Side Effect:
        sb / scoreboard : (dict)
            It will update the inital scoreboard with a new one adding the implication of shootthemoon   
    """
    for player, score in sb.items():
        if player != plyr:
            score += 26
            sb[player] = score
        else:
            score = 0
            sb[player] = score
        
    return sb





def score(trick, table, plyr=None):
    """
    Calculates a players hand.
    
    This function iterates through a dict container of players hand. Hand being a list of cards, It iterates through each card and evaluates it based on the condition to each point value.
        - If any card within a hand has the club of 'hearts' it would equal (1pt)
        - If a hand has a 'Q' of 'spade' it would equal (13pt).
    
                  
    Args:
        trick : (dict)
            This contains the players card that they placed in their trick stack
            
        table : (dict)
            This container contains the players and their hands to iterate through.
    
        plyr : (str)
            The player that wins the trick of cards from the trick stack.
            
    Returns:   
        scoreboard : (dict)
            A key value pair of the players name and the score that have with their hand.
                  
    Side Effect:
        self.scoreboard : (dict)
            Technically this will manipulate the scoreboard attribute within the gameplay class to a new scoreboard.
     
    """
    
    names = list(trick)
    plyr_flag = False
    winner = "" 
    scoreboard = {}
    pts = 0


    for player,card in trick.items():
        
        suit = card[0]
        value = card[1]
        
        scoreboard[player] = 0
        
        if player == plyr:
            winner = player
           
        
        if suit == 'heart':
                pts += 1
                #cardcount += 1               
        elif suit == 'spade' and value == 'Q':
                pts += 13
                #cardcount += 1
        else:
            continue
        
    
    
    
    if winner in names:
        scoreboard[winner] = pts
        
       
       
        
    for player, hand in table.items():
        
        cardcount = 0

        for card in hand:
            
            suit = card[0]
            value = card[1]
            

            if suit == 'heart':
                cardcount += 1  
                             
            elif suit == 'spade' and value == 'Q':
                pts += 13
                cardcount += 1
            else:
                continue
            
        
        if cardcount == 14:
            plyr_flag = player
            
        cardcount = 0
        
    if plyr_flag:
        scoreboard = shootmoon(plyr_flag, scoreboard)
        
        
    return scoreboard       

 
