def main():
    f = open('14-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    addresses = {}
    mask = ''
    for line in lines:
        if line.split(' = ')[0] == 'mask':
            mask = line.split(' = ')[1]
        else:
            addresses[line.split(' = ')[0][4:][:-1]] = binaryToDecimal(add(mask, decimalToBinary(line.split(' = ')[1])))

    total = 0
    for key, value in addresses.items():
        total += int(value)

    print('Result:', total)

def add(mask, value):
    while len(value) < 36:
        value = '0' + value

    output = ''
    index = len(value) - 1
    while index >= 0:
        value_char = value[index]
        if mask[index] == 'X':
            output = value_char + output
        else:
            output = mask[index] + output
        index -= 1
    return output

def decimalToBinary(d):
    if d == '0': return '0'
    b = ''
    i = int(d)
    x = 0
    while 2**x <= i:
        x += 1
    x -= 1
    length = x + 1
    while len(b) < length:
        if 2**x <= i:
            b += '1'
            i -= 2**x
        else:
            b += '0'
        x -= 1
    return b

def binaryToDecimal(b):
    sum = 0
    i = len(b) - 1
    while i >= 0:
        sum += int(b[i]) * 2**(len(b) - 1 - i)
        i -= 1
    return str(sum)

if __name__ == '__main__':
    main()

# Result: 9879607673316
