def main():
    total = 0
    for line in lines[139:613]:
        x = evaluate(rules['0'], line, 0, True)
        if x[0]:
            total += 1

    result = 0
    for line in lines[139:613]:
        if evaluate2(line):
            result += 1
    
    print('Result:', result)

def evaluate(criteria, line, index=0, special=False):
    if '"' in criteria:
        if line[index] == criteria[1:-1]:
            return (True, line[index])
        else: return (False, '')
    elif '|' in criteria:
        a = evaluate(criteria.split(' | ')[0], line, index)
        b = evaluate(criteria.split(' | ')[1], line, index)

        if a[0]:
            if criteria == rules['42']:
                cache42.append(a[1])
            if criteria == rules['31']:
                cache31.append(a[1])
            return a
        elif b[0]:
            if criteria == rules['42']:
                cache42.append(b[1])
            if criteria == rules['31']:
                cache31.append(b[1])
            return b
        else:
            return (False, '')
    else:
        parts = criteria.split(' ')
        matched = ''
        for part in parts:
            c = evaluate(rules[part], line, index)
            if not c[0]:
                return (False, '')
            index += len(c[1])
            matched += c[1]
        if special and matched != line:
            return (False, '')
        return (True, matched)

def evaluate2(line):
    first = True
    i = 0
    num42 = 0
    num31 = 0
    while i < len(line):
        works42 = evaluate(rules['42'], line[i:i+8], 0, True)[0]
        works31 = evaluate(rules['31'], line[i:i+8], 0, True)[0]
        if not (works42 or works31):
            return False
        if first:
            if not works42:
                first = False
                num31 += 1
            else:
                num42 += 1
        else:
            if not works31:
                return False
            else:
                num31 += 1
        i += 8

    return num42 > num31 and num31 > 0        

if __name__ == '__main__':
    f = open('19-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    rules = {}
    for line in lines[:138]:
        rules[line.split(':')[0]] = line.split(': ')[1]

    cache42 = []
    cache31 = []

    main()

# Result: 392
