from itertools import islice

def main():
    f = open('23-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    cups = []
    for char in lines[0]:
        cups.append(int(char))

    curr = cups[0]
    for i in range(0, 100):
        go = move(cups, curr)
        cups = go[0]
        curr = go[1]

    result = ''
    for cup in cups:
        result += str(cup)

    final = ''
    last = result.split('1')
    for thing in last[::-1]:
        final += thing

    print('Result:', final)

def move(cups, curr):
    dest = curr - 1
    if dest == 0: dest = 9

    pickup = []
    i = cups.index(curr) + 1
    for j in range(0, 3):
        if i == len(cups): i = 0
        pickup.append(cups[i])
        i += 1

    for element in pickup:
        cups.remove(element)

    while dest not in cups:
        dest -= 1
        if dest == 0: dest = 9

    ind = cups.index(dest)
    for element in pickup[::-1]:
        cups.insert(ind+1, element)

    prev_index = cups.index(curr)
    if prev_index == len(cups) - 1:
        next_curr = cups[0]
    else:
        next_curr = cups[prev_index + 1]

    return cups, next_curr

if __name__ == '__main__':
    main()

# Result: 
