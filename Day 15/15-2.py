def main():
    f = open('15-input.txt', 'r')
    strnums = f.read().split(',')
    f.close()

    nums = []
    for strnum in strnums:
        nums.append(int(strnum))

    i = len(nums) + 1
    numsDict = {}
    latest = nums[-1]

    for index, num in enumerate(nums[0:-1]):
        numsDict[num] = index + 1

    while i <= 30000000:
        if latest not in numsDict:
            numsDict[latest] = i - 1
            latest = 0
        else:
            time_since = i - 1 - numsDict[latest]
            numsDict[latest] = i - 1
            latest = time_since
        
        i += 1

    print('Result:', latest)

if __name__ == '__main__':
    main()

# pretty slow but not that slow!
# Result: 1047739
