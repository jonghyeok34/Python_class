# 사용자 정의 클래스

class ContactInfo:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def print_info(self):
        print("{}:{}".format(self.name, self.email))

    def __del__(self):
        print('class is deleted')

if __name__ == "__main__":
    ci = ContactInfo('jonghyeok', 'jonghyeok34@gmail.com')
    ci.print_info()
    print(id(ci))
    del ci

    ci2 = ContactInfo('jongmyeong', 'abc981125@gmail.com')
    print(id(ci2))
    ci2.print_info()

    ci3 = ContactInfo('heyji', 'hyeji2@gmail.com')
    print(id(ci3))
