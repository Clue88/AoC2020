from collections import deque
from itertools import islice

def main():
    f = open('22-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    a = lines[1:26]
    b = lines[28:53]

    for i, element in enumerate(a):
        a[i] = int(element)
    for i, element in enumerate(b):
        b[i] = int(element)

    play_game((a, b), True)

def play_game(decks, first=False):
    p1 = deque(decks[0])
    p2 = deque(decks[1])
    p1_check = [p1.copy()]
    p2_check = [p2.copy()]
    game_round = 0

    while True:
        for i in p1_check:
            if p1 == i:
                for j in p2_check:
                    if p2 == j:
                        if game_round > 0:
                            return 'P1'
    
        p1_check.append(p1.copy())
        p2_check.append(p2.copy())

        p1_card = p1.popleft()
        p2_card = p2.popleft()

        if p1_card <= len(p1) and p2_card <= len(p2):
            p1_sub = islice(p1, 0, p1_card)
            p2_sub = islice(p2, 0, p2_card)
            winner = play_game((p1_sub, p2_sub))
            if winner == 'P1':
                p1.append(p1_card)
                p1.append(p2_card)
            else:
                p2.append(p2_card)
                p2.append(p1_card)
        else:
            if p1_card > p2_card:
                p1.append(p1_card)
                p1.append(p2_card)
            else:
                p2.append(p2_card)
                p2.append(p1_card)

            if len(p1) == 0:
                if first: print('Result:', score(p2))
                return 'P2'
            elif len(p2) == 0:
                if first: print('Result:', score(p1))
                return 'P1'
        game_round += 1

def score(deck):
    score = 0
    for number in range(1, len(deck) + 1):
        score += number * deck.pop()
    return score

if __name__ == '__main__':
    main()
