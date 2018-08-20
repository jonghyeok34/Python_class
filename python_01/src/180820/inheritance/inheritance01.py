class A:  # 부모 클래스
    def __init__(self):
        self.message = "Hello World"

    def print_message(self):
        print(self.message)


class B(A):  # 자식 클래스
    pass


if __name__ == '__main__':
    a = A()
    a.print_message()

    b = B()
    b.message = "changed Message"
    b.print_message()