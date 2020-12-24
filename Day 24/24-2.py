from collections import defaultdict

def main():
    f = open('24-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    instructions = []
    for line in lines:
        instruction = []
        i = 0
        while i < len(line):
            if line[i] == 'w' or line[i] == 'e': instruction.append(line[i]); i += 1
            else: instruction.append(line[i:i+2]); i += 2
        instructions.append(instruction)

    black = set()
    for instruction in instructions:
        x = 0
        y = 0
        for part in instruction:
            if part == 'e': x += 1
            elif part == 'w': x -= 1
            elif part == 'ne': y += 1
            elif part == 'nw': x -= 1; y += 1
            elif part == 'se': x += 1; y -= 1
            elif part == 'sw': y -= 1
        
        if (x, y) in black: black.remove((x, y))
        else: black.add((x, y))

    for i in range(0, 100):
        counts = defaultdict(int)
        for tile in black:
            x = tile[0]
            y = tile[1]
            counts[(x+1, y)] += 1
            counts[(x-1, y)] += 1
            counts[(x, y+1)] += 1
            counts[(x-1, y+1)] += 1
            counts[(x+1, y-1)] += 1
            counts[(x, y-1)] += 1

        new_black = set()
        for key, value in counts.items():
            if key in black and value in [1, 2]:
                new_black.add(key)
            elif key not in black and value == 2:
                new_black.add(key)

        black = new_black

    print('Result:', len(black))

if __name__ == '__main__':
    main()

# Result: 
