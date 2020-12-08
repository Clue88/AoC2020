def main():
    f = open('8-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    visited = []
    curr = 0
    accumulator = 0
    while curr not in visited:
        visited.append(curr)
        if lines[curr].split(' ')[0] == 'nop':
            curr += 1
        elif lines[curr].split(' ')[0] == 'acc':
            accumulator += int(lines[curr].split(' ')[1])
            curr += 1
        elif lines[curr].split(' ')[0] == 'jmp':
            curr += int(lines[curr].split(' ')[1])

    print('Result:', accumulator)

if __name__ == '__main__':
    main()

# Result: 1337
