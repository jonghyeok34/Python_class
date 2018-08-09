# replace() : 특정 문자열을 다른 문자열로 바꿔주는 역할

txt = 'My password is 1234'

# 1 -> 0
ret1 = txt.replace('1', '0')
# 1 -> python
ret2 = txt.replace('1', 'python')

print('original txt = {}'.format(txt))
print("txt.replace('1', '0') = {}".format(ret1))
print("txt.replace('1', 'python') = {}".format(ret2))


txt2 = '매일 많은 일들이 일어납니다'
ret3 = txt2.replace('매일', '항상')
ret4 = txt2.replace('일', '사건')

print('original txt2 = {}'.format(txt2))
print("txt2.replace('매일', '항상') = {}".format(ret3))
print("txt2.replace('일', '사건') = {}".format(ret4))
