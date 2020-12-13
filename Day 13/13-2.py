def main():
    f = open('13-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    buses = []
    for index, element in enumerate(lines[1].split(',')):
        if element != 'x':
            buses.append((index, int(element)))
    print(buses)

    timestamp = 100000000000388
    while True:
        print(timestamp)
        passed = True
        for index, bus in buses:
            if (timestamp + index) % bus != 0:
                passed = False
                break
        if passed:
            print('Result:', timestamp)
            break
        timestamp += 643

if __name__ == '__main__':
    main()

# Took too long - used WolframAlpha instead. Theoretically could implement
# a Chinese Remainder Theorem algorithm but I'm tired and lazy.

# Result: 760171380521445
