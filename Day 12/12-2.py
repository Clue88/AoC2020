def main():
    f = open('12-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    way_x = 10
    way_y = 1
    ship_x = 0
    ship_y = 0
    direction = 0
    # E = 0, N = 1, W = 2, S = 3

    for line in lines:
        instruction = line[0]
        num = int(line[1:])
        
        if instruction == 'N': way_y += num
        elif instruction == 'S': way_y -= num
        elif instruction == 'E': way_x += num
        elif instruction == 'W': way_x -= num
        elif instruction == 'L':
            way_x -= ship_x
            way_y -= ship_y
            old_x = way_x
            old_y = way_y
            if num == 90:
                way_y = old_x
                way_x = -1 * old_y
            elif num == 180:
                way_y = -1 * old_y
                way_x = -1 * old_x
            elif num == 270:
                way_y = -1 * old_x
                way_x = old_y
            way_x += ship_x
            way_y += ship_y
        elif instruction == 'R':
            way_x -= ship_x
            way_y -= ship_y
            old_x = way_x
            old_y = way_y
            if num == 270:
                way_y = old_x
                way_x = -1 * old_y
            elif num == 180:
                way_y = -1 * old_y
                way_x = -1 * old_x
            elif num == 90:
                way_y = -1 * old_x
                way_x = old_y
            way_x += ship_x
            way_y += ship_y
        elif instruction == 'F':
            diff_x = way_x - ship_x
            diff_y = way_y - ship_y
            ship_x += num * diff_x
            way_x += num * diff_x
            ship_y += num * diff_y
            way_y += num * diff_y

    distance = abs(ship_x) + abs(ship_y)
    print('Result:', distance)

if __name__ == '__main__':
    main()

# Result: 23960
