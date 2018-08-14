def getFibonacciX(n):
    if n < 2:
        return n
    return getFibonacciX(n - 1) + getFibonacciX(n - 2)


memo = {}

def getFibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        print(memo)
        return memo[n]
    else:
        memo[n]=getFibonacci(n - 1) + getFibonacci(n - 2)
        return memo[n]


def getFibonacci2(n):
    a, b = 1, 0
    for i in range(n):
        a, b = b, a + b
    return b


n = int(input('몇 번쨰 피보나치 수열을 구합니까?'))

x = [1, 1]
for d in range(2, n):
    x.append(1)
    x[d] = x[d - 1] + x[d - 2]
print('%d번쨰 값:%s' % (n, x[n - 1]))

print(getFibonacci(n))
print(getFibonacci2(n))
