# keys() : 딕셔너리에서 key만 추출하는 함수

names = {'Mary': 10999, 'Sams': 2111, 'Amy': 9778, 'Tom': 20245,
         'Micheal': 27115, 'Bob': 5887, 'Kelly': 7855}

ks = names.keys()
print('ks:', ks)

for k in ks:
    print("Key: %s\t Value: %s" % (k, names[k]))
#
print('--------------------------------')
for k in names.keys():
    print("Key: %s\t Value: %s" % (k, names[k]))
