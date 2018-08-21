# stockcode.txt 파일의 모든 내용을 읽어와 출력
# readlines() : 파일의 끝까지 한 줄씩 읽어와서 각 줄을 리스트로 리턴
# readlines() - 텍스트 파일의 모든 내용을 한꺼번에 읽어오기 때문에 파일의 크기가 매우 큰 경우 메모리 부족 문제 발생

f = open('stockcode.txt', 'r')
lines = f.readlines()
print(lines)
print(type(lines))
print(enumerate(lines))

for num, line in enumerate(lines):
    print('%d %s' % (num + 1, line), end='')

f.close()
