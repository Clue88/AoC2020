done = {}

def main():
    f = open('10-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    nums = []
    for line in lines:
        nums.append(int(line))

    nums.sort()
    nums.insert(0, 0)
    print('Result:', ways_to_end(0, nums))

def ways_to_end(index, nums):
    if len(nums) - 1 == index:
        return 1

    if index in done.keys():
        return done[index]
        
    total = 0
    possibles = []
    if (nums[index] + 1) in nums:
        possibles.append(nums[index] + 1)
    if (nums[index] + 2) in nums:
        possibles.append(nums[index] + 2)
    if (nums[index] + 3) in nums:
        possibles.append(nums[index] + 3)
    
    for possible in possibles:
        total += ways_to_end(nums.index(possible), nums)

    done[index] = total
    return total

if __name__ == '__main__':
    main()

# Result: 9256148959232
