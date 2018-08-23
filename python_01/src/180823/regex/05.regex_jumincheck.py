# 주민 번호가 형식이 맞는지 정규 표현식으로 처리

import re

# 주민번호 정규식
def checkIdWithRegex(num):
    p = re.compile("(\d{6})-?(\d{7})")
    if p.search(num) != None:
        print('올바른 주민번호입니다')
    else:
        print('올바른 주민번호가 아닙니다.')

num = '100000-2000000'
checkIdWithRegex(num)



num='1000000-200000000'
checkIdWithRegex(num)
