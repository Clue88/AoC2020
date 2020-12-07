def main():
    f = open('7-input.txt', 'r')
    rules = f.read().split('\n')[:-1]
    f.close()

    total = 0
    rule_dict = {}
    for rule in rules:
        bags_initial = rule.split(',')
        bags = []
        for bag in bags_initial:
            color = ''
            started = False
            for index, char in enumerate(bag):
                if bag[index:index+3] == 'bag':
                    started = False
                if started:
                    color += char
                if char in '1234567890':
                    started = True
            bags.append(color[1:-1])
            
        rule_dict[rule.split(' bags')[0]] = bags

    curr = []
    for rule in rules:
        if 'shiny gold' in rule_dict[rule.split(' bags')[0]]:
            total += 1
            curr.append(rule.split(' bags')[0])

    for i in range(0, 10):
        new = []
        for rule in rules:
            if rule.split(' bags')[0] in curr:
                continue
            for color in curr:
                if color in rule_dict[rule.split(' bags')[0]]:
                    total += 1
                    curr.append(rule.split(' bags')[0])
                    new.append(rule.split(' bags')[0])
                    break
        temp = []
        [temp.append(x) for x in curr if x not in temp]
        curr = temp
    
    print('Result:', len(curr))

if __name__ == '__main__':
    main()

# Result: 302
