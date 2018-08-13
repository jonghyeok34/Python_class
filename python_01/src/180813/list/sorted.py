# sorted() : 리스트 요소 정렬  -기본(오름차순)
# 오름 차순 : 숫자( 1,2,3,4..)
#            문자(사전순으로 정렬)

namelist = ['Mary', "Sams", 'Amy', 'Tom', 'Micheal', 'Bob', 'Kelly']

ret1 = sorted(namelist)
print(namelist)  # 오름차순 정렬
print("ret1:", ret1)

ret2 = sorted(namelist, reverse=True)
print("ret2:", ret2)

