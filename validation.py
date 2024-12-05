

def validate_card_choice(player_name, card_choice, trick, player_hand):
    """
    Validates a player's card choice based on game rules.
    
    Args:
        player_name (str): The name of the player making the choice.
        card_choice (list): The card being played, e.g., ['club', 2].
        trick (dict): The current trick stack.
        player_hand (list): The player's current hand.
        
    Returns:
        bool: True if the card is valid, False otherwise.
        
    Side Effect:
        Prompts the player to reselect a card if invalid.
    """
    valid = False
    if len(trick) == 0:  
        if card_choice[0] == 'heart':  
            non_heart_exists = False
            for card in player_hand:
                if card[0] != 'heart':
                    non_heart_exists = True
            if non_heart_exists:  
                print(f"{player_name}, you cannot lead with a heart on the first trick.")
                valid = False
            else:
                valid = True
        else:
            valid = True
    else:  
        first_card = list(trick.values())[0]
        first_suit = first_card[0]
        suit_found = False
        for card in player_hand:
            if card[0] == first_suit:
                suit_found = True
        if suit_found:  
            if card_choice[0] == first_suit:
                valid = True
            else:
                print(f"{player_name}, you must follow the suit: {first_suit}.")
                valid = False
        else:  
            valid = True

    if valid:
        return True
    else:
        return False
