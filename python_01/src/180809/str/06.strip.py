# 문자열 좌,우의 공백제거 : lstrip(), rstrip(), strip()
# lstrip(): 문자열 좌측의 공백을 없애주는 함수
# rstrip(): 문자열 우측의 공백을 없애주는 함수
# strip(): 문자열 좌,우의 공백을 없애주는 함수

txt ='  양쪽에 공백이 있는 문자입니다    '

afterLstrip = txt.lstrip()
afterRstrip = txt.rstrip()
afterStrip = txt.strip()

print("txt = <%s>" % txt)
print("txt.lstrip() : <%s>" % afterLstrip)
print("txt.rstrip() : <%s>" % afterRstrip)
print("txt.strip()  : <%s>" % afterStrip)