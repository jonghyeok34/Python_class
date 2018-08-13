# shuffle() : 리스트 요소를 무작위로 섞어주는 함수

# from 모듈명 import 함수명

from random import shuffle

listdata = list(range(1,10))
s_data = listdata
print(listdata)

for i in range(3):
    shuffle(s_data)
    print(s_data)