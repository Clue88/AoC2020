def main():
    f = open('25-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    card = int(lines[0])
    door = int(lines[1])
    subject = 7

    card_loop = 0
    door_loop = 0

    value = 1
    i = 0
    while card_loop == 0 or door_loop == 0:
        i += 1
        value = (value * subject) % 20201227
        if value == card: card_loop = i
        if value == door: door_loop = i

    i = 0
    subject = card
    value = 1
    while i < door_loop:
        value = (value * subject) % 20201227
        i += 1

    print('Result:', value)

if __name__ == '__main__':
    main()

# Result: 
