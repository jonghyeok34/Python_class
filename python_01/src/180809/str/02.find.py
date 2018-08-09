# find(): 문자열에서 특정 문자 위치를 index 로 구해주는 역할

txt = 'A lot of things occur each day, every day'

# 가장 먼저 나오는 'e'의 index 번호를 리턴
offset1 = txt.find('e')

# 가장 먼저 나오는 'day'의 index 번호를 리턴
offset2 = txt.find('day')

# index 번호 30번 이후에 나오는 'day'의 index 번호를 리턴
offset3 = txt.find('day', 30)

print("txt.find('e'):", offset1)  # 22
print("txt.find('day'):", offset2)  # 27
print("txt.find('day', 30):", offset3)  # 38
