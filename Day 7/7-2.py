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

    nums_dict = {}
    for rule in rules:
        nums = []
        for char in rule:
            if char in '1234567890':
                nums.append(int(char))
        nums_dict[rule.split(' bags')[0]] = nums

    print('Result:', find_num_bags(rule_dict, nums_dict, 'shiny gold'))
    

def find_num_bags(rule_dict, nums_dict, color):
    if rule_dict[color] == ['']:
        return 0
    
    total = 0
    for index, in_color in enumerate(rule_dict[color]):
        value = nums_dict[color][index] * find_num_bags(rule_dict, nums_dict, in_color)
        value += nums_dict[color][index]
        total += value

    return total
    

if __name__ == '__main__':
    main()

# Result: 4165
