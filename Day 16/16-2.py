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

    accepted = []

    for line in lines[25:261]:
        bad = False
        for value in line.split(','):
            passed = 0
            for rule, entry in rules.items():
                num = int(value)
                if not (num < entry[0] or num > entry[3] or (num > entry[1] and num < entry[2])):
                    passed += 1
            if passed == 0:
                bad = True
                break
        if not bad:
            accepted.append(line)

    for index, line in enumerate(accepted):
        accepted[index] = line.split(',')

    determined = {}

    for rule, entry in rules.items():
        i = 0
        determined[rule] = []
        while i < 20:
            failed = False
            for line in accepted:
                num = int(line[i])
                if num < entry[0] or num > entry[3] or (num > entry[1] and num < entry[2]):
                    failed = True
                    break
            if not failed and i not in determined.values():
                determined[rule].append(i)
            i += 1
        
    i = 0
    final = {}
    while i < 20:
        for key, value in determined.items():
            if len(value) == 1:
                found = value[0]
                final[key] = found
                for key, value in determined.items():
                    if found in value: value.remove(found)
                break
        i += 1

    your_ticket = lines[22].split(',')
    total = 1
    total *= int(your_ticket[final['departure location']])
    total *= int(your_ticket[final['departure station']])
    total *= int(your_ticket[final['departure platform']])
    total *= int(your_ticket[final['departure track']])
    total *= int(your_ticket[final['departure date']])
    total *= int(your_ticket[final['departure time']])

    print('Result:', total)

if __name__ == '__main__':
    main()

# Result: 3429967441937
