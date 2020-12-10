def main():
    f = open('10-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    nums = []
    for line in lines:
        nums.append(int(line))

    nums.sort()
    nums.append(nums[-1] + 3)
    ones = 1
    threes = 0

    i = 0
    while i < len(nums) - 1:
        if nums[i+1] - nums[i] == 1:
            ones += 1
        else:
            threes += 1
        i += 1

    print('Result:', ones * threes)

if __name__ == '__main__':
    main()

# Result: 1914
