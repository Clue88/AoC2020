import re
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
        fields = []
        lines = passport.split('\n')

        for line in lines:
            elements = line.split(' ')
            for element in elements:
                keys.append(element.split(':')[0])
                fields.append(element.split(':'))

        keys.sort()
        fields.sort()

        if 'cid' in keys:
            keys.remove('cid')
        if keys != required:
            continue

        if len(fields) == 8:
            fields.pop(1)
        
        if int(fields[0][1]) < 1920 or int(fields[0][1]) > 2002:
            continue
        if int(fields[5][1]) < 2010 or int(fields[5][1]) > 2020:
            continue
        if int(fields[2][1]) < 2020 or int(fields[2][1]) > 2030:
            continue
        if fields[4][1][-2:] not in ['cm', 'in']:
            continue
        if 'cm' in fields[4][1] and (int(fields[4][1].split('cm')[0]) < 150 or int(fields[4][1].split('cm')[0]) > 193):
            continue
        if 'in' in fields[4][1] and (int(fields[4][1].split('in')[0]) < 59 or int(fields[4][1].split('in')[0]) > 76):
            continue
        if not re.match("#[(a-f)(0-9)]+", fields[3][1]):
            continue
        if fields[1][1] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            continue
        if not re.match("[(0-9)]{9}", fields[6][1]) or len(fields[6][1]) != 9:
            continue

        total += 1

    print('Result:', total)

if __name__ == '__main__':
    main()

# Result: 145
