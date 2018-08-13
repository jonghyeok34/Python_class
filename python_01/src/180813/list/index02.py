# index()  리스트에서 특정 요소 인덱스 번호

solarsys =['태양', '수성', '금요일,', '지구', '화성', '목성',' 토성','천왕성', '해왕성']
planet='지구'

# index 3번
pos = solarsys.index(planet)
print("%s는 태양계에서 %d번째에 위차히고 있습니다" % (planet, pos))

# index 9번
planet= '해왕성'
pos = solarsys.index(planet, 5)
print("%s는 태양계에서 %d번째에 위차히고 있습니다" % (planet, pos))


