def main():
    f = open('20-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    tiles = {}
    i = 0
    while i < len(lines):
        tiles[lines[i][5:9]] = lines[i+1:i+11]
        i += 12
    
    sides = []

    for key, tile in tiles.items():
        sides.append(tile[0])
        sides.append(tile[-1])
        vertical1 = ''
        vertical2 = ''
        for line in tile:
            vertical1 += (line[0])
            vertical2 += (line[-1])
        sides.append(vertical1)
        sides.append(vertical2)

    sides_single = []
    for item in sides:
        if sides.count(item) + sides.count(item[::-1]) == 1:
            sides_single.append(item)

    corners = []
    for key, tile in tiles.items():
        north = tile[0]
        south = tile[-1]
        east = ''
        west = ''
        for line in tile:
            east += line[-1]
            west += line[0]
        
        total = 0
        if north in sides_single: total += 1
        if south in sides_single: total += 1
        if east in sides_single: total += 1
        if west in sides_single: total += 1

        if total == 2:
            corners.append(key)

    result = 1
    for corner in corners:
        result *= int(corner)

    print('Result:', result)

if __name__ == '__main__':
    main()

# Result: 
