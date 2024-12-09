
def announce_turn(player_name, player_hand=None):
    """
    Announces the current player's turn and optionally shows their hand.
    Only reveals all player hands after all names have been input.
    
    Primary Author: Hamza

    Args:
        player_name (str): The name of the current player whose turn it is.
        player_hand (list, optional): The player's current hand of cards. Default is None.

    Returns:
        None
    """
    if player_hand:
        print(f"\n--- It's {player_name}'s turn ---")
        print(f"{player_name}'s hand: {', '.join([f'{card[1]} of {card[0]}' for card in player_hand])}")
    else:
        print(f"\n--- It's {player_name}'s turn ---")
