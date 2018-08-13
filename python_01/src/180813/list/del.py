# index()  리스트에서 특정 요소 인덱스 번호

solarsys =['태양', '수성', '금성,', '지구' '화성', '목성' ,
           ' 토성']
planet='지구'


del solarsys[0]
print(solarsys)

#index 1~2
del solarsys[1:3]
print(solarsys)

#리스트 자체를 메모리상에서 제거
del solarsys
# print(solarsys)