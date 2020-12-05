def main():
    f = open('5-input.txt', 'r')
    seats = f.read().split('\n')[:-1]
    f.close()

    ids = []
    for seat in seats:
        row_sum = 0
        row = seat[0:7]
        for ind, char in enumerate(row[::-1]):
            if char == 'B': row_sum += 2 ** int(ind)

        col_sum = 0
        col = seat[7:]
        for ind, char in enumerate(col[::-1]):
            if char == 'R': col_sum += 2 ** int(ind)
        
        ids.append(int(row_sum) * 8 + int(col_sum))

    for id in ids:
        if id + 2 in ids and not id + 1 in ids:
            result = id + 1
            break

    print('Result:', result)

if __name__ == '__main__':
    main()

# Result: 527
