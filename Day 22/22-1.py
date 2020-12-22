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

    while len(a) != 0 and len(b) != 0:
        if a[0] > b[0]:
            a.append(a[0])
            a.append(b[0])
            a = a[1:]
            b = b[1:]
        else:
            b.append(b[0])
            b.append(a[0])
            a = a[1:]
            b = b[1:]

    score = 0
    if len(a) > 0:
        for i, card in enumerate(a[::-1]):
            score += (i+1) * card
    else:
        for i, card in enumerate(b[::-1]):
            score += (i+1) * card

    print('Result:', score)

if __name__ == '__main__':
    main()

# Result: 
