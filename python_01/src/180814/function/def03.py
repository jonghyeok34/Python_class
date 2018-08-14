# 최대값 구하는 함수

def max(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3


# 최소값 구하는 함수
def min(n1, n2, n3):
    if n1 <= n2 and n1 <= n3:
        return n1
    elif n2 <= n1 and n2 <= n3:
        return n2
    else:
        return n3


print('3개의 정수를 입력하세요')
n1 = int(input())
n2 = int(input())
n3 = int(input())
print(n1, n2, n3)

max = max(n1, n2, n3)
min = min(n1, n2, n3)

print('큰 값:', max)
print('작은 값:', min)
