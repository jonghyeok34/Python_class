class Animal:  # 멤버 변수
    name = 'dog'
    age = 5


class Animal2:  # 멤버 변수
    __name = 'dog'
    __age = 5

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age


a1 = Animal()  # 인스턴스 생성
print(a1.name)
print(a1.age)

a1.name = "원숭이"
a1.age = 10
print(a1.name)
print(a1.age)

print('<< animal2 >>')
a2 = Animal2()
print(a2.getName())
print(a2.getAge())

a2.setName('원숭이')
a2.setAge(10)

# print(a2.name)
print(a2.getName())
print(a2.getAge())
