# 절대값 구하기:
def abs(n):
    if n < 0:
        n = -n
    return n


result = abs(-30)
print('절대값:', result)
