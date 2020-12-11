def main():
    f = open('11-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    old_lines = []
    i = 0
    while old_lines != lines:
    # while i < 3:
        i+= 1
        old_lines = []
        for line in lines:
            old_lines.append(line)

        y = 0
        x = 0
        change = []
        while y < len(lines):
            while x < len(lines[y]):
                total = surrounding(y, x, lines)
                if lines[y][x] == 'L' and total == 0:
                    change.append((y, x))
                if lines[y][x] == '#' and total >= 5:
                    change.append((y, x))
                x += 1
            x = 0
            y += 1

        for seat in change:
            if lines[seat[0]][seat[1]] == 'L':
                row = list(lines[seat[0]])
                row[seat[1]] = '#'
                lines[seat[0]] = ''.join(row)
            else:
                row = list(lines[seat[0]])
                row[seat[1]] = 'L'
                lines[seat[0]] = ''.join(row)

    occupied = 0
    for line in lines:
        for char in line:
            if char == '#': occupied += 1

    print('Result:', occupied)

def surrounding(y, x, lines):
    orig_y = y
    orig_x = x
    total = 0

    while y > 0:
        y -= 1
        if lines[y][x] == 'L':
            break
        if lines[y][x] == '#':
            total += 1
            break
    y = orig_y
    x = orig_x

    while y < len(lines) - 1:
        y += 1
        if lines[y][x] == 'L':
            break
        if lines[y][x] == '#':
            total += 1
            break
    y = orig_y
    x = orig_x

    while x > 0:
        x -= 1
        if lines[y][x] == 'L':
            break
        if lines[y][x] == '#':
            total += 1
            break
    y = orig_y
    x = orig_x

    while x < len(lines[y]) - 1:
        x += 1
        if lines[y][x] == 'L':
            break
        if lines[y][x] == '#':
            total += 1
            break
    y = orig_y
    x = orig_x

    while x > 0 and y > 0:
        y -= 1
        x -= 1
        if lines[y][x] == 'L':
            break
        if lines[y][x] == '#':
            total += 1
            break
    y = orig_y
    x = orig_x

    while x < len(lines[y]) - 1 and y > 0:
        y -= 1
        x += 1
        if lines[y][x] == 'L':
            break
        if lines[y][x] == '#':
            total += 1
            break
    y = orig_y
    x = orig_x

    while x > 0 and y < len(lines) - 1:
        y += 1
        x -= 1
        if lines[y][x] == 'L':
            break
        if lines[y][x] == '#':
            total += 1
            break
    y = orig_y
    x = orig_x

    while x < len(lines[y]) - 1 and y < len(lines) - 1:
        y += 1
        x += 1
        if lines[y][x] == 'L':
            break
        if lines[y][x] == '#':
            total += 1
            break
    y = orig_y
    x = orig_x

    return total

if __name__ == '__main__':
    main()

# Result: 
