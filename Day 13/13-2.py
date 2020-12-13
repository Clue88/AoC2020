def main():
    f = open('13-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    buses = []
    product = 1
    for index, element in enumerate(lines[1].split(',')):
        if element != 'x':
            buses.append((-1 * index, int(element)))
            product *= int(element)
    
    total = 0
    for rem, mod in buses:
        if mod == 0:
            continue
        value = (rem * (product // mod) * (invert_modulo((product // mod), mod)))
        total += value

    print('Result:', total % product)

def extended_euclid(a, b):
    if b == 0:
        return (1, 0)
    (x, y) = extended_euclid(b, a % b)
    k = a // b
    return (y, x - k * y)

def invert_modulo(a, n):
    (b, x) = extended_euclid(a, n)
    if b < 0:
        b = (b % n + n) % n
    return b

if __name__ == '__main__':
    main()

# Result: 760171380521445
