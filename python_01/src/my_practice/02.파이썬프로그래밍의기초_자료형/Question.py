# q1

pin = "881120-1068234"
yymmdd = pin.split('-')[0]
# yymmdd = pin[:6]
num = pin.split('-')[1]
# num = pin[7:]

print(yymmdd)
print(num)

# q2

print(pin.split('-')[1][0])
# print(pin[7])

# q3
a = [1, 3, 5, 4, 2]
a.sort()
print(a)
a.reverse()
print(a)

# q4
a = ['Life', 'is', 'too', 'short']
print(a[0] + " " + a[1] + " " + a[2] + " " + a[3])
# print(" ".join(a))