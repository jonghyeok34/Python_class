# for 문: dictionary

# for i in 딕셔너리

dic = {'애플': 'www.apple.com',
       '파이썬': 'www.python.org',
       '마이크로소프트': 'www.microsoft.com'
       }

for k, v in dic.items():
    print('{0}:{1}'.format(k, v))