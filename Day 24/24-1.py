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

    flipped = []
    
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
        
        if [x, y] in flipped: flipped.remove([x, y])
        else: flipped.append([x, y])

    print('Result:', len(flipped))

if __name__ == '__main__':
    main()

# Result: 
