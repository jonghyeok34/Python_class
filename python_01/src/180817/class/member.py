# 클래스변수, 멤버변수

#

class student:
    schoolName = "Korea"


class student_i:
    schoolName = "Korea"
    name = ""
    def setName(self, name):
        self.name = name

    def getname(self):
        return self.name


if __name__ == "__main__":

    # 클래스변수 -> 클래스와 클래스로부터 만들어진 객체 모두가 공유
    stu1 = student()
    stu2 = student()
    print("stu1의 주소:{}".format(id(stu1)))
    print("stu2의 주소:{}".format(id(stu2)))

    student.schoolName = "Seoul"

    print("Student의 주소:{}".format(student.schoolName))
    print("stu1의 주소:{}".format(stu1.schoolName))
    print("stu2의 주소:{}".format(stu2.schoolName))

    # 인스턴스 변수
    stu_i1 = student_i()
    stu_i2 = student_i()
    stu_i1.setName("Steve Jobs")
    stu_i2.setName("Steve Wozniak")
    print("stu1의 이름:{} ".format(stu_i1.getname()))
    print("stu2의 이름:{} ".format(stu_i2.getname()))
