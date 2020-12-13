def main():
    f = open('13-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    buses = []
    for element in lines[1].split(','):
        if element != 'x':
            buses.append(int(element))

    estimate = int(lines[0])
    smallest = 1000000000000
    smallest_bus = 0
    for bus in buses:
        if bus - (estimate % bus) < smallest:
            smallest = bus - (estimate % bus)
            smallest_bus = bus

    print('Result:', smallest * smallest_bus)

if __name__ == '__main__':
    main()

# Result: 3464
