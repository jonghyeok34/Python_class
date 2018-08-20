# 클래스 상속

class Add:  # 부모
    def add(self, n1, n2):
        return n1 + n2


class Calculator(Add):  # 자식
    def sub(self, n1, n2):
        return n1 - n2


obj = Calculator()
print(obj.add(10, 20))
print(obj.sub(10, 20))
