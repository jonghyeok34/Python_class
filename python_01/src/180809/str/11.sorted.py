# sorted() : 문자열 정렬
# sorted() - 특정 변수에 저장된 값을 오름 차순으로 정렬해주는 역할
# e.g) 오름 차순 : 1,2,3 .. 사전순

strdata = input('정렬할 문자열을 입력하세요: ')
ret1 = (sorted(strdata))
ret2 = (sorted(strdata, reverse=True))

print('strdata:', strdata)
print('sorted(strdata):', ret1)
print('sorted(strdata, reverse=True):', ret2)
