def scope():
    global a
    a = 1


a = 10
print('a=', a)
scope()
print('a=', a)
