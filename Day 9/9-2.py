def main():
    f = open('9-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    contiguous = []
    for index, line in enumerate(lines):
        first = index
        sum = 0
        while sum < 1212510616:
            sum += int(lines[index])
            index += 1
        if sum == 1212510616:
            contiguous = lines[first:index]
            if len(contiguous) < 2:
                contiguous = []
            else:
                biggest = 0
                smallest = 1300505067051622
                for i in contiguous:
                    if int(i) > biggest:
                        biggest = int(i)
                    if int(i) < smallest:
                        smallest = int(i)

                print('Result:', biggest + smallest)
                return

if __name__ == '__main__':
    main()

# Result: 171265123
