# 포맷 문자열
#  %s     문자열
#  %c     문자나 기호 1개
#  %d     정수
#  %f     실수
#  %%     %


txt1 = '자바'
txt2 = '파이썬'
num1 = 5
num2 = 10

print('나는 %s보다 %s에 익숙합니다.' % (txt1, txt2))
print('%s는 %s보다 %d배 더 쉽습니다..' % (txt1, txt2, num1))
print("%d+%d =%d" % (num1, num2, num1+num2))
print('작년 세계 경제 성장률 %d에 비해 %d%% 증가했다.' % (num1, num2))

# 문자열에서 변하는 값을 나타내는 문자열 % 기호를 사용
