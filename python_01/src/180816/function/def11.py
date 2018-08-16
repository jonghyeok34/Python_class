import time

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

start_time = time.time()

print("3!=", fact(3))
print("5!=", fact(5))
print("7!=", fact(7))
print("10!=", fact(10))
print("32!=", fact(32))
print("997!=", fact(997))

print("--- %s seconds ---" % (time.time() - start_time))