from collections import OrderedDict

def main():
    f = open('6-input.txt', 'r')
    s = f.read()
    groups = s[:-1].split('\n\n')
    f.close()

    total = 0
    for group in groups:
        group = group.replace('\n', '')
        group = ''.join(OrderedDict.fromkeys(group)) 
        total += len(group)

    print('Result:', total)

if __name__ == '__main__':
    main()

# Result: 6259
