import re

p = re.compile('blue|white|red')

print(p.sub('color', 'blue socks and red shoes'))

# 1번만 변경됨
print(p.sub('color', 'blue socks and red shoes', count=1))
