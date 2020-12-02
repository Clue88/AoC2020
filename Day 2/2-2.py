def main():
    f = open('2-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    total = 0
    for line in lines:
        target = line.split(':')[0][-1]
        password = line.split(':')[1][1:]
        indexes = line.split(' ')[0].split('-')
        
        if (password[int(indexes[0]) - 1] == target) != (password[int(indexes[1]) - 1] == target):
            total += 1
    
    print('Result:', total)

if __name__ == '__main__':
    main()

# Result: 308
