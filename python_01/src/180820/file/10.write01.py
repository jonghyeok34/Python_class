text = input("파일에 저장할 내용을 입력하세요")

with open('data1.txt', 'w', encoding='utf-8') as file:
    file.write(text)
