def main():
    f = open('3-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    ind = 0
    trees = 0
    for line in lines:
        if line[ind] == '#':
            trees += 1
        ind += 3
        ind = ind % 31

    print('Result:', trees)

if __name__ == '__main__':
    main()

# Result: 189
