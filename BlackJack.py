import random
import time

tryagain_valid = ['y', 'yes']
tryagain = 'yes'

deck = []


for i in range(4):
    deck.append([])
    for j in range(13):
        deck[i].append(True)


type_card = [' of hearts', ' of diamonds', ' of spades', ' of clubs']
name = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
p_hand = []
cpu_hand = []

def gen_card(d):
    cont = False
    while not cont:
        suit = random.randint(0,3)
        value = random.randint(0, 12)
        cont = d[suit][value]
        d[suit][value] = False
    return (suit, value)

def sum_hand(hand):
    return sum(value[x[1]] for x in hand)

def print_hand(hand):
    for i in hand:
        print(str(name[i[1]]) + type_card[i[0]])
    print('Score: ' + str(sum_hand(hand)))
    
p_hand.append(gen_card(deck))
p_hand.append(gen_card(deck))
cpu_hand.append(gen_card(deck))

while sum_hand(p_hand) < 21 and sum_hand(cpu_hand) < 21:    
    print('You have:')
    print_hand(p_hand)
    print('CPU has:')
    print_hand(cpu_hand)
    print('Do you want to draw another card?')
    t = input()
    
    if t == 'yes' or t == 'y':
        p_hand.append(gen_card(deck))
        if sum_hand(cpu_hand) < 17:
            cpu_hand.append(gen_card(deck))
    else:
        while sum_hand(cpu_hand) < 17:
            if sum_hand(cpu_hand) > sum_hand(p_hand):
                break
            else:
                cpu_hand.append(gen_card(deck))
        break

p_score = sum_hand(p_hand)
cpu_score = sum_hand(cpu_hand)

print('You have:')
print_hand(p_hand)
print('CPU has:')
print_hand(cpu_hand)

if p_score <= 21:
    if p_score > cpu_score:
        print('You win')
    elif p_score == cpu_score:
        print('You tied')
    else:
        if cpu_score <= 21:
            print('You lose')
        else:
            print('You win') ## You win despite lower score since CPU score > 21
else:
    if cpu_score <= 21:
        print('You lose')
    else:
        print('You both lose')
print('\nGAME OVER\n')

