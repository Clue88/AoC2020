def main():
    f = open('15-input.txt', 'r')
    strnums = f.read().split(',')
    f.close()

    nums = []
    for strnum in strnums:
        nums.append(int(strnum))

    i = len(nums)
    while len(nums) < 2020:
        if nums[i-1] not in nums[0:i-1]:
            nums.append(0)
        else:
            j = len(nums) - 2
            while j >= 0:
                if nums[j] == nums[i-1]:
                    nums.append(i-1 - j)
                    break
                j -= 1
        i += 1

    print('Result:', nums[-1])

if __name__ == '__main__':
    main()

# Result: 517
