#1부터 ~n까지 합
def sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print('1부터', n, '까지의 합=', sum)

print(sum(5))