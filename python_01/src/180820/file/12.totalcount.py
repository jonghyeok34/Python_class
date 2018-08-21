with open('data.txt', 'r') as f:
    data = f.read()
    tmp = data.split()
    print(tmp)
    print(type(tmp))
    print('단어수 : [%d]' % len(tmp))
