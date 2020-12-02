def main():
    f = open('2-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    total = 0
    for line in lines:
        target = line.split(':')[0][-1]
        password = line.split(':')[1][1:]
        interval = line.split(' ')[0]
        occur = 0
        for char in password:
            if char == target:
                occur += 1
        if occur >= int(interval.split('-')[0]) and occur <= int(interval.split('-')[1]):
            total += 1
    
    print('Result:', total)

if __name__ == '__main__':
    main()

# Result: 456
