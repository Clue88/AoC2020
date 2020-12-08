def main():
    f = open('8-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    result = 0
    for index, line in enumerate(lines):
        if line.split(' ')[0] != 'acc':
            attempt = test(index, lines)
            if attempt != -1:
                result = attempt
                break

    print('Result:', result)

def test(index, lines):
    new_lines = []
    for line in lines:
        new_lines.append(line)

    if new_lines[index].split(' ')[0] == 'nop':
        new_lines[index] = new_lines[index].replace('nop', 'jmp')
    else:
        new_lines[index] = new_lines[index].replace('jmp', 'nop')

    visited = []
    curr = 0
    accumulator = 0
    while curr not in visited:
        visited.append(curr)
        if curr == len(new_lines):
            return accumulator

        if new_lines[curr].split(' ')[0] == 'nop':
            curr += 1
        elif new_lines[curr].split(' ')[0] == 'acc':
            accumulator += int(new_lines[curr].split(' ')[1])
            curr += 1
        elif new_lines[curr].split(' ')[0] == 'jmp':
            curr += int(new_lines[curr].split(' ')[1])

    visited.append(curr)
    return -1

if __name__ == '__main__':
    main()

# Result: 1358
