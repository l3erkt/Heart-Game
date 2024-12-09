# ♣️♦️ Heart's Game ♠️♥️

#### Description:
For INST326 me and my group members Kyle, Melat, and Hamza decided to create the famous game called Hearts in Python based on our knowledge of the game.

![Wave](https://media.giphy.com/media/j65N3HZsImyTeVhmSy/giphy.gif)



## Purpose of each file
```
deck.py 
This contains a dictionary that formats the card deck before it is dealt to the players.
```


```
deal.py
This file contains code that deals cards to players and also takes in plauer names to name each player.
```

```
score.py
This file contains functions that count a players hand and calculates their score.
```

```
validation.py
This file validates a player's choice of card, whether it means verifying that the players follows the lead suit or that they don't play a heart suit first
```


```
game.py
The purpose of this file to run the program because it contains most of the game logic and it starts the program.
```


```
visual.py
This file creates a bar graph that shows the scores of each player
```


```
announce.py
The purpose of this file is to announce the sequence of turns in the game. It determines and displays the order in which players will play their cards during a round.
```



## Instructions - (How to run program)
```Python
  step 1: Enter terminal/command line
  step 2: type "python game.py" and hit enter key
  
```



## Instructions - (How to use program)
```Python
  step 1: The program will first prompt you to enter the names of 4 players
  step 2: It will then deal cards and the person who has the 2 of clubs will go first
  step 3: The program will print the hand of the player with each card separated by a "|". Each player will first tell the program the suit they have to play, it must match the leading suit, and then it will ak for a number.
```



## Annotated bibliography

“Copy in Python (Deep Copy and Shallow Copy).” Geeksforgeeks.Org, 26 July 2024, www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/. I had a problem with copying a specific data structure in my program, I tried directly making a shallow copy but it wouldn't work correctly. This source helped me remember how to make a deep copy in python

“Learn to Play Hearts.” Bicyclecards.Com, bicyclecards.com/how-to-play/hearts/. Accessed 2 Dec. 2024. This source helped me understand the rules for the heart game. It provided guidance on rules, gameplay, scoring, etc.



## Attribution
| Method/Function | Primary Author | Technique Demonstrated |
|   :--------     |    :------:    |      ------------      |
|  `__str__()`    |    Kyle    | magic methods, f-strings containing expressions|
|  `gameplay()`   |    Kyle    |                            |
| `deal()`        |   Bereket  |                            | 
| `table()`       |   Bereket  |                            | 
| `winner()`      |   Bereket  | Key function               |
| `bar_graph()`   |   Bereket  | data with pyplot           |
| `done()`        |   Bereket  |                            | 
| `score()`       |   Bereket  |                            |  
|`convert_card()` |    Melat   |sequence unpacking, conditional expressions.|
| `validate_card_choice()` |  Hamza   | keyword arguements, generator exp|
| `announc.py()`    |  Hamza    | comprehensions              |

#### Collaborator's GitHub
- [@l3erkt](https://github.com/l3erkt)
- [@kylewon12](https://github.com/kylewon12)
- [@melatabera](https://github.com/melatabera)
- [@himziman](https://github.com/himziman)
