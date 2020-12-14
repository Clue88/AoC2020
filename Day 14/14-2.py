def main():
    f = open('14-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    addresses = {}
    mask = ''
    for i, line in enumerate(lines):
        if line.split(' = ')[0] == 'mask':
            mask = line.split(' = ')[1]
        else:
            address = line.split(' = ')[0][4:][:-1]
            result = apply_mask(decimalToBinary(address), mask)
            value = line.split(' = ')[1]
            possibles = iterate_possibles(result)
            for possible in possibles:
                addresses[possible] = value

    total = 0
    for key, value in addresses.items():
        total += int(value)

    print('Result:', total)

def apply_mask(address, mask):
    while len(address) < 36:
        address = '0' + address

    output = ''
    index = len(address) - 1
    while index >= 0:
        address_char = address[index]
        if mask[index] == '0':
            output = address_char + output
        else:
            output = mask[index] + output
        index -= 1
    return output

def iterate_possibles(result):
    possibles = []

    if 'X' not in result:
        possibles.append(result)
        return possibles

    for char in result:
        if char == 'X':
            check = []
            for possible in possibles:
                check.append(binaryToDecimal(possible))
            possibles += iterate_possibles(result.replace('X', '0', 1))
            possibles += iterate_possibles(result.replace('X', '1', 1))
            break
    
    if 'X' not in result:
        possibles.append(result)
    return possibles

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

# Result: 
