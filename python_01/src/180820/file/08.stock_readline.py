f = open('stockcode.txt', 'r')
num = 1
line = f.readline()

while line != '':
    print('%d %s' % (num, line), end='')
    line = f.readline()
    num += 1

f.close()
