# 예외처리 : try ~ except Exception as e

# 코드에서 예외 발생 내용을 확인 할 떄 사용

try:
    print("안녕하세요")
    print(1/0)
except Exception as e:
    print(e)