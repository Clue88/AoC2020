def main():
    f = open('18-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    total = 0
    for line in lines:
        total += evaluate(line)

    print('Result:', total)

def evaluate(expression):
    if '(' not in expression:
        parts = expression.split(' ')
        while '+' in parts:
            new_parts = []
            i = 0
            while i < len(parts):
                if i == len(parts) - 1:
                    new_parts.append(parts[i])
                    break
                if parts[i+1] == '+':
                    replacement = int(parts[i]) + int(parts[i+2])
                    new_parts.append(replacement)
                    i += 3
                else:
                    new_parts.append(parts[i])
                    i += 1
            parts = new_parts
                
        total = int(parts[0])
        if len(parts) == 1:
            return total
        
        i = 1
        while i < len(parts):
            if parts[i] == '+':
                total += int(parts[i+1])
            else:
                total *= int(parts[i+1])
            i += 2
    else:
        while '(' in expression:
            big_parentheses = find_inner_parentheses(expression)
            parentheses = big_parentheses[1:-1]
            expression = expression.replace(big_parentheses, str(evaluate(parentheses)))

        parts = expression.split(' ')
        while '+' in parts:
            new_parts = []
            i = 0
            while i < len(parts):
                if i == len(parts) - 1:
                    new_parts.append(parts[i])
                    break
                if parts[i+1] == '+':
                    replacement = int(parts[i]) + int(parts[i+2])
                    new_parts.append(replacement)
                    i += 3
                else:
                    new_parts.append(parts[i])
                    i += 1
            parts = new_parts
                
        total = int(parts[0])
        if len(parts) == 1:
            return total
        
        i = 1
        while i < len(parts):
            if parts[i] == '+':
                total += int(parts[i+1])
            else:
                total *= int(parts[i+1])
            i += 2
    return total

def find_inner_parentheses(expression):
    start = -1
    end = -1
    for index, char in enumerate(expression):
        if char == '(':
            start = index
        if char == ')':
            end = index
            break
    return expression[start:end+1]
        

if __name__ == '__main__':
    main()

# Result: 20394514442037
