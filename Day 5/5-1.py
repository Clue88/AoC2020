def main():
    f = open('5-input.txt', 'r')
    seats = f.read().split('\n')[:-1]
    f.close()

    highest = 0
    for seat in seats:
        row_sum = 0
        row = seat[0:7]
        for ind, char in enumerate(row[::-1]):
            if char == 'B': row_sum += 2 ** int(ind)

        col_sum = 0
        col = seat[7:]
        for ind, char in enumerate(col[::-1]):
            if char == 'R': col_sum += 2 ** int(ind)

        if int(row_sum) * 8 + int(col_sum) > highest:
            highest = int(row_sum) * 8 + int(col_sum)

    print('Result:', highest)

if __name__ == '__main__':
    main()

# Result: 959
