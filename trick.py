stack = {'kyle': ['club', 7], 'bk': ['club', 4], 'melat': ['club', 3], 'hamza': ['club', 'J']}



def trick(trk):


    first_plyr_card = trk[list(trk)[0]]
    
    
    convrt_cards = []
    for plyr, card in trk.items():
        suit = card[0]
        num = card[1]
        
        if num == 'J':
            num = 11
            convrt_cards.append([suit, num])
            
        elif num == 'Q':
            num = 12
            convrt_cards.append([suit, num])

        elif num == 'K':
            num = 13
            convrt_cards.append([suit, num])
                    
        elif num == 'A':
            num = 14
            convrt_cards.append([suit, num])
                    
        else:
            convrt_cards.append([suit, num])

    sorted_cards = sorted(convrt_cards, reverse=True, key=lambda card: card[1])



trick(stack)