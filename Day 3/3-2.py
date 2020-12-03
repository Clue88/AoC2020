def main():
    f = open('3-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    total = 1
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    for x, y in slopes:
        ind = 0
        trees = 0
        for num, line in enumerate(lines):
            if num % y != 0:
                continue
            if line[ind] == '#':
                trees += 1
            ind += x
            ind = ind % 31
        total *= trees

    print('Result:', total)

if __name__ == '__main__':
    main()

# Result: 1718180100
