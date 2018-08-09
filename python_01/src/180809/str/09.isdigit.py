# isdigit() : 숫자인지 문자인지 판별
# 문자열 구성하는 요소가 모두 숫자이면 True/ 아니면 False

txt1 = '010-1234-5678'
txt2 = 'R2D2'
txt3 = '1212'

ret1 = txt1.isdigit()
ret2 = txt2.isdigit()
ret3 = txt3.isdigit()

print("Is {} digit? {}".format(txt1, ret1))
print("Is {} digit? {}".format(txt2, ret2))
print("Is {} digit? {}".format(txt3, ret3))
