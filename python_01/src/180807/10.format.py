# format() : 출력 형식을 지정해서 출력

print('Hello', 'World!')
print('Hello {0}, {1}'.format('World!', "Okay"))

name = input('input your name: ')
job = input('input your job: ')

print('{} is a {}'.format(name, job))
print('{1} is a {0}'.format(name, job))
print('Good {n} is a {j}'.format(n=name, j=job))


