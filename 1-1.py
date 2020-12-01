def main():
    nums = []
    while True:
        num = input()
        if num:
            nums.append(int(num))
        else:
            break

    for num_a in nums:
        for num_b in nums:
            if num_a + num_b == 2020:
                print('Result: ' + str(num_a) + ' * ' + str(num_b) + ' = ' + str(num_a * num_b))
                return

if __name__ == '__main__':
    main()

# Result: 1162 * 858 = 996996
