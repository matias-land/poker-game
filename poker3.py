import random
def array_of_cards(x):
    cards = ['h2','h3','h4','h5','h6','h7','h8','h9','ht','hj','hq','hk','ha',
    's2','s3','s4','s5','s6','s7','s8','s9','st','sj','sq','sk','sa',
    'c2','c3','c4','c5','c6','c7','c8','c9','ct','cj','cq','ck','ca',
    'd2','d3','d4','d5','d6','d7','d8','d9','dt','dj','dq','dk','da']
    result_cards = []
    for i in range(x):
        val = random.randint(0,len(cards)-1)
        result_cards.append(cards[val])
        cards.pop(val)
    print(cards)
    return(result_cards)