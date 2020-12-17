def main():
    f = open('17-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    z_dim = 14 + 1
    y_dim = 14 + len(lines)
    x_dim = 14 + len(lines[0])
    grid = []
    for z in range(0, z_dim):
        grid.append([])
        for y in range(0, y_dim):
            grid[z].append([])
            for x in range(0, x_dim):
                grid[z][y].append('.')

    for y, y_value in enumerate(lines):
        for x, x_value in enumerate(y_value):
            grid[7][y+7][x+7] = x_value

    for i in range(0, 6):
        to_inactive = []
        to_active = []
        z = 1
        while z < len(grid) - 1:
            y = 1
            while y < len(grid[z]) - 1:
                x = 1
                while x < len(grid[z][y]) - 1:
                    num = neighbors(z, y, x, grid)
                    if grid[z][y][x] == '#':
                        if not (num == 2 or num == 3):
                            to_inactive.append([z, y, x])
                    else:
                        if num == 3:
                            to_active.append([z, y, x])
                    x += 1
                y += 1
            z += 1

        for cube in to_inactive:
            grid[cube[0]][cube[1]][cube[2]] = '.'
        for cube in to_active:
            grid[cube[0]][cube[1]][cube[2]] = '#'

    total = 0
    for z in grid:
        for y in z:
            for x in y:
                if x == '#':
                    total += 1

    print('Result:', total)

def print_grid(grid):
    for z in grid:
        print('\n')
        for index, y in enumerate(z):
            print(index, y)

def neighbors(z, y, x, grid):
    total = 0
    if grid[z-1][y-1][x-1] == '#': total += 1
    if grid[z-1][y-1][x] == '#': total += 1
    if grid[z-1][y-1][x+1] == '#': total += 1
    if grid[z-1][y][x-1] == '#': total += 1
    if grid[z-1][y][x] == '#': total += 1
    if grid[z-1][y][x+1] == '#': total += 1
    if grid[z-1][y+1][x-1] == '#': total += 1
    if grid[z-1][y+1][x] == '#': total += 1
    if grid[z-1][y+1][x+1] == '#': total += 1
    
    if grid[z][y-1][x-1] == '#': total += 1
    if grid[z][y-1][x] == '#': total += 1
    if grid[z][y-1][x+1] == '#': total += 1
    if grid[z][y][x-1] == '#': total += 1
    if grid[z][y][x+1] == '#': total += 1
    if grid[z][y+1][x-1] == '#': total += 1
    if grid[z][y+1][x] == '#': total += 1
    if grid[z][y+1][x+1] == '#': total += 1

    if grid[z+1][y-1][x-1] == '#': total += 1
    if grid[z+1][y-1][x] == '#': total += 1
    if grid[z+1][y-1][x+1] == '#': total += 1
    if grid[z+1][y][x-1] == '#': total += 1
    if grid[z+1][y][x] == '#': total += 1
    if grid[z+1][y][x+1] == '#': total += 1
    if grid[z+1][y+1][x-1] == '#': total += 1
    if grid[z+1][y+1][x] == '#': total += 1
    if grid[z+1][y+1][x+1] == '#': total += 1

    return total

if __name__ == '__main__':
    main()

# Result: 380
