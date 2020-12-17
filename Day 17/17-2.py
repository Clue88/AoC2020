def main():
    f = open('17-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    w_dim = 14 + 1
    z_dim = 14 + 1
    y_dim = 14 + len(lines)
    x_dim = 14 + len(lines[0])
    grid = []
    for w in range(0, w_dim):
        grid.append([])
        for z in range(0, z_dim):
            grid[w].append([])
            for y in range(0, y_dim):
                grid[w][z].append([])
                for x in range(0, x_dim):
                    grid[w][z][y].append('.')

    for y, y_value in enumerate(lines):
        for x, x_value in enumerate(y_value):
            grid[7][7][y+7][x+7] = x_value

    for i in range(0, 6):
        to_inactive = []
        to_active = []
        w = 1
        while w < len(grid) - 1:
            z = 1
            while z < len(grid[w]) - 1:
                y = 1
                while y < len(grid[w][z]) - 1:
                    x = 1
                    while x < len(grid[w][z][y]) - 1:
                        num = neighbors(w, z, y, x, grid)
                        if grid[w][z][y][x] == '#':
                            if not (num == 2 or num == 3):
                                to_inactive.append([w, z, y, x])
                        else:
                            if num == 3:
                                to_active.append([w, z, y, x])
                        x += 1
                    y += 1
                z += 1
            w += 1

        for cube in to_inactive:
            grid[cube[0]][cube[1]][cube[2]][cube[3]] = '.'
        for cube in to_active:
            grid[cube[0]][cube[1]][cube[2]][cube[3]] = '#'

    total = 0
    for w in grid:
        for z in w:
            for y in z:
                for x in y:
                    if x == '#':
                        total += 1

    print('Result:', total)

def print_grid(grid):
    for w in grid:
        print('\n')
        print('\n')
        for z in w:
            print('\n')
            for index, y in enumerate(z):
                print(index, y)

def neighbors(w, z, y, x, grid):
    total = 0
    if grid[w-1][z-1][y-1][x-1] == '#': total += 1
    if grid[w-1][z-1][y-1][x] == '#': total += 1
    if grid[w-1][z-1][y-1][x+1] == '#': total += 1
    if grid[w-1][z-1][y][x-1] == '#': total += 1
    if grid[w-1][z-1][y][x] == '#': total += 1
    if grid[w-1][z-1][y][x+1] == '#': total += 1
    if grid[w-1][z-1][y+1][x-1] == '#': total += 1
    if grid[w-1][z-1][y+1][x] == '#': total += 1
    if grid[w-1][z-1][y+1][x+1] == '#': total += 1
    
    if grid[w-1][z][y-1][x-1] == '#': total += 1
    if grid[w-1][z][y-1][x] == '#': total += 1
    if grid[w-1][z][y-1][x+1] == '#': total += 1
    if grid[w-1][z][y][x-1] == '#': total += 1
    if grid[w-1][z][y][x] == '#': total += 1
    if grid[w-1][z][y][x+1] == '#': total += 1
    if grid[w-1][z][y+1][x-1] == '#': total += 1
    if grid[w-1][z][y+1][x] == '#': total += 1
    if grid[w-1][z][y+1][x+1] == '#': total += 1

    if grid[w-1][z+1][y-1][x-1] == '#': total += 1
    if grid[w-1][z+1][y-1][x] == '#': total += 1
    if grid[w-1][z+1][y-1][x+1] == '#': total += 1
    if grid[w-1][z+1][y][x-1] == '#': total += 1
    if grid[w-1][z+1][y][x] == '#': total += 1
    if grid[w-1][z+1][y][x+1] == '#': total += 1
    if grid[w-1][z+1][y+1][x-1] == '#': total += 1
    if grid[w-1][z+1][y+1][x] == '#': total += 1
    if grid[w-1][z+1][y+1][x+1] == '#': total += 1

    
    if grid[w][z-1][y-1][x-1] == '#': total += 1
    if grid[w][z-1][y-1][x] == '#': total += 1
    if grid[w][z-1][y-1][x+1] == '#': total += 1
    if grid[w][z-1][y][x-1] == '#': total += 1
    if grid[w][z-1][y][x] == '#': total += 1
    if grid[w][z-1][y][x+1] == '#': total += 1
    if grid[w][z-1][y+1][x-1] == '#': total += 1
    if grid[w][z-1][y+1][x] == '#': total += 1
    if grid[w][z-1][y+1][x+1] == '#': total += 1
    
    if grid[w][z][y-1][x-1] == '#': total += 1
    if grid[w][z][y-1][x] == '#': total += 1
    if grid[w][z][y-1][x+1] == '#': total += 1
    if grid[w][z][y][x-1] == '#': total += 1
    if grid[w][z][y][x+1] == '#': total += 1
    if grid[w][z][y+1][x-1] == '#': total += 1
    if grid[w][z][y+1][x] == '#': total += 1
    if grid[w][z][y+1][x+1] == '#': total += 1

    if grid[w][z+1][y-1][x-1] == '#': total += 1
    if grid[w][z+1][y-1][x] == '#': total += 1
    if grid[w][z+1][y-1][x+1] == '#': total += 1
    if grid[w][z+1][y][x-1] == '#': total += 1
    if grid[w][z+1][y][x] == '#': total += 1
    if grid[w][z+1][y][x+1] == '#': total += 1
    if grid[w][z+1][y+1][x-1] == '#': total += 1
    if grid[w][z+1][y+1][x] == '#': total += 1
    if grid[w][z+1][y+1][x+1] == '#': total += 1


    if grid[w+1][z-1][y-1][x-1] == '#': total += 1
    if grid[w+1][z-1][y-1][x] == '#': total += 1
    if grid[w+1][z-1][y-1][x+1] == '#': total += 1
    if grid[w+1][z-1][y][x-1] == '#': total += 1
    if grid[w+1][z-1][y][x] == '#': total += 1
    if grid[w+1][z-1][y][x+1] == '#': total += 1
    if grid[w+1][z-1][y+1][x-1] == '#': total += 1
    if grid[w+1][z-1][y+1][x] == '#': total += 1
    if grid[w+1][z-1][y+1][x+1] == '#': total += 1
    
    if grid[w+1][z][y-1][x-1] == '#': total += 1
    if grid[w+1][z][y-1][x] == '#': total += 1
    if grid[w+1][z][y-1][x+1] == '#': total += 1
    if grid[w+1][z][y][x-1] == '#': total += 1
    if grid[w+1][z][y][x] == '#': total += 1
    if grid[w+1][z][y][x+1] == '#': total += 1
    if grid[w+1][z][y+1][x-1] == '#': total += 1
    if grid[w+1][z][y+1][x] == '#': total += 1
    if grid[w+1][z][y+1][x+1] == '#': total += 1

    if grid[w+1][z+1][y-1][x-1] == '#': total += 1
    if grid[w+1][z+1][y-1][x] == '#': total += 1
    if grid[w+1][z+1][y-1][x+1] == '#': total += 1
    if grid[w+1][z+1][y][x-1] == '#': total += 1
    if grid[w+1][z+1][y][x] == '#': total += 1
    if grid[w+1][z+1][y][x+1] == '#': total += 1
    if grid[w+1][z+1][y+1][x-1] == '#': total += 1
    if grid[w+1][z+1][y+1][x] == '#': total += 1
    if grid[w+1][z+1][y+1][x+1] == '#': total += 1

    return total

if __name__ == '__main__':
    main()

# Result: 2332
