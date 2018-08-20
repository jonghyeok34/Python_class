# 정적메소드

# 1 공유를 목적으로 하기 위해 주로 사용
# 2.메소드 위에 @staticmethod 데이코레이터 사용
# 3. ' 클래스.정적메소드 호출

class Calculator:
    @staticmethod
    def plus(a, b):
        return a + b

    @staticmethod
    def minus(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b


if __name__ == "__main__":
    a = 3
    b = 2
    print("{}+{}={}".format(a, b, Calculator.plus(a, b)) )
    print("{}-{}={}".format(a, b, Calculator.minus(a, b)) )
    print("{}*{}={}".format(a, b, Calculator.multiply(a, b)) )
    print("{}/{}={}".format(a, b, Calculator.divide(a, b)) )
