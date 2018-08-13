# index()  리스트에서 특정 요소 인덱스 번호

solarsys =['태양', '수성', '금성,', '지구' '화성', '목성' ,
           ' 토성']
planet='지구'

# index 3번
pos = solarsys.index(planet)
print("%s는 태양계에서 %번쩨에 위차히고 있습니다".format(planet, pos))

# index 9번
pos = solarsys.index('planet',5)
print("%s는 태양계에서 %번쩨에 위차히고 있습니다".format(planet,pos))

