def main():
    f = open('16-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    rules = {}
    for line in lines[0:20]:
        nums = []
        entry = line.split(': ')[1]
        nums.append(int(entry.split('-')[0]))
        nums.append(int(entry.split('-')[1].split(' ')[0]))
        nums.append(int(entry.split('-')[1].split(' ')[-1]))
        nums.append(int(entry.split('-')[-1]))
        rules[line.split(':')[0]] = nums

    total = 0
    for line in lines[25:261]:
        for value in line.split(','):
            passed = 0
            for rule, entry in rules.items():
                num = int(value)
                if not (num < entry[0] or num > entry[3] or (num > entry[1] and num < entry[2])):
                    passed += 1
            if passed == 0:
                total += int(value)

    print('Result:', total)

if __name__ == '__main__':
    main()

# Result: 21071
