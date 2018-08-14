# 난수 발생

import random

# 0.0 ~1.0 사이의 실수형으로 난수 발생
r1 = random.random()
print('r1:', r1)


# 난수: 1~10 사이 정수
r2 = random.randint(1, 10)
print('r2:', r2)


# 난수: 1~45 사이 정수
r3 = random.randint(1, 45)
print('r3:', r3)


# 리스트 항목 중 1개 추출
rainbow = ['빨', '주', '노', '초', '파', '남', '보']
r4 = random.choice(rainbow)
print('r4:', r4)
