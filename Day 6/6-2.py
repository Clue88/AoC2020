def main():
    f = open('6-input.txt', 'r')
    s = f.read()
    groups = s[:-1].split('\n\n')
    f.close()

    total = 0
    for group in groups:
        persons = group.split('\n')
        common = 'abcdefghijklmnopqrstuvwxyz'
        for person in persons:
            for char in common:
                if char not in person:
                    common = common.replace(char, '')
        total += len(common)

    print('Result:', total)

if __name__ == '__main__':
    main()

# Result: 3178
