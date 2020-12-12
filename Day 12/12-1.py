def main():
    f = open('12-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    x = 0
    y = 0
    direction = 0
    # E = 0, N = 1, W = 2, S = 3

    for line in lines:
        instruction = line[0]
        num = int(line[1:])
        if instruction == 'F':
            if direction == 0:
                x += num
            elif direction == 1:
                y += num
            elif direction == 2:
                x -= num
            elif direction == 3:
                y -= num
        elif instruction == 'N': y += num
        elif instruction == 'S': y -= num
        elif instruction == 'E': x += num
        elif instruction == 'W': x -= num
        elif instruction == 'L': direction = (direction + num / 90) % 4
        elif instruction == 'R': direction = (direction - num / 90) % 4

    distance = abs(x) + abs(y)
    print('Result:', distance)

if __name__ == '__main__':
    main()

# Result: 1589
