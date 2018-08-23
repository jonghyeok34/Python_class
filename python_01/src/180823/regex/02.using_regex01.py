# 정규 표현식을 사용해 뒷자릴ㄹ\를 7 시간 닌
import re

data = """
park 800905-1049118
kim  700905-1059119
"""

# 주민 번호에 대한 패턴 설정

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))
