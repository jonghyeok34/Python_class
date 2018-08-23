# 정규식을 이용한 문자열 검색

# 함수           기능
# -------------------
# match()        문자열의 처음부터 정규식과 매치되는지 검사
# search()       문자열 전체를 검색해 정규식과 매치되는지 검사
# findall()      정규식과 매치되는 모든 문자열을 리스트로 리턴
# finditer()     정규식과 매치되는 모든 문자열을 iter객체로 리턴

import re

# 영문자(a~z) 정규 표현식
p = re.compile('[a-z]+')

# 1.match()
m = p.match('python')
print(m)

m = p.match('3 python')
print(m)                # 패턴과 일치되지 않으면 None 리턴


# search()
m = p.search('python')
print(m)

m = p.search('3 python')
print(m)

# findall()
result = p.findall('life is too short')
print(result)

# finditer()
result = p.finditer('life is too short')
print(result)

for r in result:
    print(r)
