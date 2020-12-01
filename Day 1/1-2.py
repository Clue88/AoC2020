def main():
    f = open('1-input.txt', 'r')
    nums = f.read().split('\n')[:-1]
    f.close()

    for num_a in nums:
        for num_b in nums:
            for num_c in nums:
                if int(num_a) + int(num_b) + int(num_c) == 2020:
                    print('Result: ' + num_a + ' * ' + num_b + ' * ' + num_c + ' = ' + str(int(num_a) * int(num_b) * int(num_c)))
                    return

if __name__ == '__main__':
    main()

# Result: 282 * 19 * 1719 = 9210402
