def plus(a, b):
    return a+b

print(plus(1, 2))

def greet():
    return 'Hi'

#입력값 x

a = greet()
print(a)

# 결과값 x 함수

def sum2(a, b):
    print("%d, %d의 합은 %d입니다." % (a,b, a+b))


# 입력값이 몇 개인지 모를 때

def sum_many(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

result = sum_many(1,2,3,4)
print(result)

result2 =  sum_many(1,2,3,4,5,6,7,7)
print(result2)

def sum_mul(choice,*args):
    if choice== 'sum':
        result = 0
        for i in args:
            result += i
    if choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result

result  = sum_mul('mul',1,2,3,4,5,6,7)
print(result)
result  = sum_mul('sum',1,2,3,4,5,6,7)
print(result)

# 함수 결과 값

def sum_and_mul(a,b):
    return a+b, a*b

result = sum_and_mul(3,4)
sum, mul = sum_and_mul(3,4)
print("sum is", sum)
print("mul is", mul)

def say_nick(nick):
    if nick=='바보':
        return
    print('나의 별명은 %s입니다.' % nick )
    
say_nick('바보')
say_nick('굿')


def say_myself(name,old, man=True):
    print("나의 이름은 %s입니다" % name)
    print("나의 나이는 %d입니다" % old)
    if man:
        print('남자입니다.')
    else:
        print('여자입니다.')

say_myself('박종혁', 23)

# def say_myself2(name,man=True,old):  # non-default parameter follows default parameter
#     print("나의 이름은 %s입니다" % name)
#     print("나의 나이는 %d입니다" % old)
#     if man:
#         print('남자입니다.')
#     else:
#         print('여자입니다.')


a=1
def vartest():
    global a
    a += 1

vartest()
print(a)

