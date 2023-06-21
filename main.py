import random
cards = []
suits = ["spades", "clubs", "hearts", "diamonds"]
ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","k"]
for suit in suits:
    for rank in ranks:
     cards.append([suit, rank])


def shuffle_cards():
   random.shuffle(cards)

def deal_cards(number):
    cards_dealt = []

    for x in range(number):
         card = cards.pop()
         cards_dealt.append(card)
    return cards_dealt

shuffle_cards()

cards_dealt = deal_cards(2)
card = cards_dealt[0]
rank = card[1]
if rank == "A":
    value = 11
elif rank == "J" or rank == "K" or rank == "Q":
    value = 10
else:
    value = rank    

rank_dict = {"rank": rank, "value": value}

print(value, rank)        
