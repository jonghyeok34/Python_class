# 클래스의 다중상속

class Add:  # 부모클래스
    def add(self, n1, n2):
        return n1 + n2


class Multiply:
    def multiply(self, n1, n2):
        return n1 * n2


class Calculator(Add, Multiply):
    def subtract(self, n1, n2):
        return n1 - n2


if __name__ == "__main__":
    cal = Calculator()
    print(cal.add(10, 2))
    print(cal.multiply(10, 2))
