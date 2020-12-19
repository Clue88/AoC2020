def main():
    total = 0
    for line in lines[139:613]:
        x = evaluate(rules['0'], line, 0, True)
        if x[0]:
            total += 1

    print('Result:', total)

def evaluate(criteria, line, index=0, special=False):
    if '"' in criteria:
        if line[index] == criteria[1:-1]:
            return (True, line[index])
        else: return (False, '')
    elif '|' in criteria:
        a = evaluate(criteria.split(' | ')[0], line, index)
        b = evaluate(criteria.split(' | ')[1], line, index)
        if a[0]:
            return a
        elif b[0]:
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

if __name__ == '__main__':
    f = open('19-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    rules = {}
    for line in lines[:138]:
        rules[line.split(':')[0]] = line.split(': ')[1]

    main()

# Result: 187
