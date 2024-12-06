
def validate_card_choice(player_name, card_choice, 
                         trick, player_hand, allow_heart_lead=False):
    """
    Validates a player's card choice based on game rules.
    Primary Author: Hamza
    Rubric 7D Techniques used: 
        - Keyword Arguments
        - Generator Expressions

    Args:
        player_name (str): Name of the player making the choice.
        card_choice (list): The card being played, e.g., ['club', 2].
        trick (dict): The current trick stack.
        player_hand (list): The player's current hand.
        allow_heart_lead (bool, optional): Whether to allow hearts to lead the 
                                            first trick (default: False).  
                                            
    Returns:
        bool: True if the card is valid, False otherwise.
    
    """
    
    # using as default assumption
    valid = True 
    
    if len(trick) > 0:
        
        # extracting the suit of first card
        first_suit = list(trick.values())[0][0] 
        
        # generator exp to check if player has any card matching first suit
        has_suit = any(card[0] == first_suit for card in player_hand)
        
        if has_suit and card_choice[0] != first_suit:
            print(f"{player_name}, you must follow the suit: {first_suit}")
            valid = False
            
    else: 
        # keyword arg used for first trick-soecific validation
        if not allow_heart_lead and card_choice[0] == 'heart':
            
            # checking if player has naything other than heart
            has_non_heart = any(card[0] != 'heart' for card in player_hand)
            
            
            # prevent leading with hearts if non-hearts are available
            if has_non_heart:
                print(f"{player_name}, you cannot lead with a heart on the first trick.")
                valid = False
                
    return valid