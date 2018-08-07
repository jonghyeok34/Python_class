# 멤버 연산자 :in ,not in
# in :컬렉션에 포함되어있으면 True, 포함되어있지 않으면 False;
# not in: 컬렉션에 포함되어있지 않으면 True, 포함되어 있으면 false

list =[1, 2, 3, 4, 5]

result1 = 5 in list
result2 = 4 not in list
print('result1=', result1)
print('result2=', result2)

str = 'abcde'
result3 = 'c' in str
result4 = 'k' not in str
print('result3=', result3)
print('result4=', result4)