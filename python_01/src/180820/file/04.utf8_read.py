# 2바이트 문자열이 저장된 greetings_utf8.txt 파일을
# 읽어와서 출력

with open('greetings_utf8.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

    for line in lines:
        print(line, end='')
