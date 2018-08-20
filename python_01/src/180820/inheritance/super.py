# super

class A:
    def __init__(self):
        print("A.__init__()")
        self.message = 'Hello'


class B(A):  # 자식클래스
    def __init__(self):  # 생성자
        print("B.__init__()")
        super().__init__()
        print(self.message)


if __name__ == "__main__":
    a = A()
    b = B()
