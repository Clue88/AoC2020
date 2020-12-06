import sys
import os
import wget

PythonTemplate = '''def main():
    f = open('//DAY//-input.txt', 'r')
    lines = f.read().split('\\n')[:-1]
    f.close()

    # code

    print('Result:')

if __name__ == '__main__':
    main()

# Result: 
'''

ShellTemplate = '''python3 //DAY//-1.py
python3 //DAY//-2.py
'''

def main():
    day = sys.argv[1]
    os.mkdir('Day ' + day)
    directory = 'Day ' + day
    files = 0

    for i in range(1, 3):
        f = open(os.path.join(directory, day + '-' + str(i) + '.py'), 'x')
        f.write(PythonTemplate.replace('//DAY//', day))
        f.close()
        files += 1

    f = open(os.path.join(directory, day + '.sh'), 'x')
    f.write(ShellTemplate.replace('//DAY//', day))
    f.close()
    files += 1

    print('Wrote ' + str(files) + ' files to directory Day ' + day)

if __name__ == '__main__':
    main()
