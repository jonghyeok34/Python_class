# split(): 문자열을 구분자(separator)로 구분되어 있는 문자열을
#          파싱(parsing)하는 역할

url = 'http://www.naver.com/news/today=20180809'
log = 'name:홍길동 age:17 sex:남자 nation:조선'

# url 변수에 저장된 데이털르 구분자('/')로 파싱함
ret1 = url.split('/')
print(ret1)

# log변수에 저장된 데이터를 공백으로 파싱함
ret2 = log.split()
print(ret2)
for data in ret2:
    d1, d2 = data.split(":")
    print('%s -> %s' % (d1, d2))

