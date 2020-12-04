def main():
    f = open('4-input.txt', 'r')
    s = f.read()
    passports = s[:-1].split('\n\n')
    f.close()

    total = 0
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    required.sort()

    for passport in passports:
        keys = []

        lines = passport.split('\n')
        for line in lines:
            elements = line.split(' ')
            for element in elements:
                keys.append(element.split(':')[0])

        keys.sort()
        if 'cid' in keys:
            keys.remove('cid')
        if keys == required:
            total += 1

    print('Result:', total)

if __name__ == '__main__':
    main()

# Result: 247
