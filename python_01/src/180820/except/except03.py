# 예외처리 : try ~ except ~ else

'''
try:
    예외가 발생할 가능성 있는 문장
except:
    예외가 발생하면 수행할 코드
finally:
    except절이 수행 여부에 상관없이 됨
'''

try:
    print('안녕하세요')
    print(1/0)
except:
    print("예외가 발생")
finally:
    print("무조건 실행")