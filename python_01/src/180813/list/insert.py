# insert() : 리스트 '특정 위치'에 요소 삽입

solarsys =['태양', '수성', '금요일,', '지구', '화성', '목성',' 토성','천왕성','해왕성']

#목성의 index 구하기
planet='목성'
pos = solarsys.index(planet)
print("pos:",pos)

# index 5번째 위치에 소행성 삽입
solarsys.insert(pos,'소행성')

print(solarsys)
