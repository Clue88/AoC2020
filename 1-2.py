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
            for num_c in nums:
                if num_a + num_b + num_c == 2020:
                    print('Result: ' + str(num_a) + ' * ' + str(num_b) + ' * ' + str(num_c) + ' = ' + str(num_a * num_b * num_c))
                    return

if __name__ == '__main__':
    main()

# Result: 282 * 19 * 1719 = 9210402
