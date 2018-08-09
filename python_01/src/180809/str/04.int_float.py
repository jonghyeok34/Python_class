# 자료형 변환: int(), float(), str()
# int() : 문자를 정수형으로 형변환
# float() : 문자를 실수형으로 형변환
# str() : 숫자를 문자로 형변환


numstr = input('숫자를 입력하세요: ')

try:
    num = int(numstr)
    print('당신이 입력한 숫자는 정수 %d입니다' % num)

except:
    try:
        num = float(numstr)
        print('당신이 입력한 숫자는 실수 %f입니다' % num)
    except:
        print('당신이 입력한 것은 숫자가 아닙니다.')
