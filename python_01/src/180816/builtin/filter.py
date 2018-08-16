# filter() : 내장 함수
# 컬렉션과 labmda 함수를 매개 변수로 받아서 컬렉션의 모든 데이터를
# lambda 함수의 매개 변수로 대입해 결과가 참인 경우만 return

li = [1, 2, 3, 4, 5]

print('lambda와 filter를 이용한 실행')
result = list(filter(lambda x: x % 2 == 0, li))
print("result=", result)
