# map()
# 인자를 바꾸어가며 함수를 반복호출해 결과를 리턴 받는 함수

f = lambda x: x * x
li = [1, 2, 3, 4, 5]

# map() 은 리스트 데이터를 lambda의 인자 x에 전달
# x*x 리턴
ret = list(map(f, li))  # li의 요소를 f함수에 전달 --> 반복 수행
print("ret1:", ret)

