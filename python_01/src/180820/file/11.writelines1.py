# 키보드로 입력한 내용을 텍스트 파일에 한줄씩 저장 - writelines() 함수

print('파일에 내용을 저장하려면, 내용을 입력하고 \n'
      '더이상 저장하지 않으려면 Enter를 누르세요')

count = 1
data = []
while True:
    text = input("[%d] 파일에 저장할 내용을 입력하세요" % count)
    if text == '':
        break
    data.append(text + '\n')
    count += 1

    with open('data2.txt', 'w', encoding='utf-8') as f:
        f.writelines(data)
