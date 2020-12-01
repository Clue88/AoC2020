def main():
    f = open('1-input.txt', 'r')
    nums = f.read().split('\n')[:-1]
    f.close()

    for num_a in nums:
        for num_b in nums:
            if int(num_a) + int(num_b) == 2020:
                print('Result: ' + num_a + ' * ' + num_b + ' = ' + str(int(num_a) * int(num_b)))
                return

if __name__ == '__main__':
    main()

# Result: 1162 * 858 = 996996
