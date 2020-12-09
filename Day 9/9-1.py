def main():
    f = open('9-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    result = 0
    for index, line in enumerate(lines):
        attempt = check(index, int(line), lines)
        if attempt != -1:
            result = attempt
            break

    print('Result:', result)

def check(index, num, lines):
    if index < 25:
        return -1
    
    for a in lines[index-25:index]:
        for b in lines[index-25:index]:
            if int(a) != int(b) and int(a) + int(b) == num:
                return -1
    return num

if __name__ == '__main__':
    main()

# Result: 1212510616
