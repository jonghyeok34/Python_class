# 예외처리 : try ~ except ~ else

'''
try:
    예외가 발생할 가능성 있는 문장
except:
    예외가 발생하면 수행할 코드
else:
    except절이 수행 안 될 경우만 실행됨
'''

try:
    print('안녕하세요')
    print(1/0)
except:
    print("예외가 발생")
else:
    print("예외가 발생하지 않았습니다")