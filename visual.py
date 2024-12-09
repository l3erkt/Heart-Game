import pandas as pd
import matplotlib.pyplot as plt


def bar_graph(board):
    """
   After game is finished a bar graph showing scores from each player would be shown.
         
    Args:
        board : (dict)
            The final cycle of the scoreboard representing the winner and losers
            
    Returns:   
        N/A
                     
    Side Effect:
        N/A 
    """
    
    p = []
    s = []
    
    for plyr, score in board.items():
        p.append(plyr)
        s.append(score)

    # Create DataFrame with correct column mapping
    df = pd.DataFrame({'Players': p, 'Score': s})
    df.plot.bar(x='Players', y='Score', legend=False)
    plt.title("Scoreboard")
    plt.ylabel("Score")
    plt.xlabel("Players")
    plt.show()