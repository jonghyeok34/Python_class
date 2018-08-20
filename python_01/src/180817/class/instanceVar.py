# 사용자 정의 클래스

class ClassVar:
    def __init__(self):
        self.text_list = []

    def add(self, text):
        self.text_list.append(text)

    def print_list(self):
        print(self.text_list)


if __name__ == '__main__':

    a = ClassVar()
    a.add('apple')
    a.add('banana')
    a.print_list()

    b = ClassVar()
    b.add('dog')
    b.add('cat')
    b.print_list()
