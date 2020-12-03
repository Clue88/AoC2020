def main():
    f = open('3-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    total = 1
    slopes = [1, 3, 5, 7]

    for slope in slopes:
        ind = 0
        trees = 0
        for line in lines:
            if line[ind] == '#':
                trees += 1
            ind += slope
            ind = ind % 31
        total *= trees

    ind = 0
    trees = 0
    for num, line in enumerate(lines):
        if num % 2 != 0:
            continue
        if line[ind] == '#':
            trees += 1
        ind += 1
        ind = ind % 31
    total *= trees

    print('Result:', total)

if __name__ == '__main__':
    main()

# Result: 1718180100
