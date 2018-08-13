# slice : 리스트 특정 구간에 있는 요소 추출
# [start index번호 : end-1 index번호]
# [1:4] index번호 1번 부터 3번까지 추출
# [4:] 4번 index부터 끝까지 추출
solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', ' 토성', '천왕성', '해왕성']

rock_planets = solarsys[1:5]
gas_planets = solarsys[5:]
print('태양계 암석형 행성:', rock_planets)
print('태양계 가스형 행성:', gas_planets)
