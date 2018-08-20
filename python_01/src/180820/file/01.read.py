# test.txt 파일 내용을 읽어서 출력


# 읽기 모드로 test.txt 파일 열기
file = open('test.txt', 'r', encoding='UTF-8')

# test.txt 파일의 모든 내용을 읽어와서 str변수에 저장
str = file.read()
print(str)

# 파일 닫기
file.close()
