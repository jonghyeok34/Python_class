class Car:
    def __init__(self):  # 생성자
        self.color = 0xFF0000  # 자동차 색깔
        self.wheel_size = 16  # 바퀴크기
        self.displacement = 2000  # 엔진 배기량

    def forward(self):
        print('전진')

    def backward(self):
        print('후진')

    def turn_left(self):
        print('좌회전')

    def turn_right(self):
        print('우회전')


if __name__ == '__main__':
    my_car = Car()
    print('0x{:02x}'.format(my_car.color))
    print(my_car.wheel_size)
    print(my_car.displacement)
    my_car.forward()
