# 텍스트 파일(data.txt)에서 키보드로 입력한 단어의 개수


def countWord(filename, word):
    with open(filename, 'r') as f:
        text = f.read()
        text = text.lower()  # 소문자로 변환
        pos = text.find(word)
        # find() : 전달된 단어의 index 번호 구함

        count = 0
        while pos != -1:  # find(): 찾고자 하는 번호가 없을 때 -1 리턴
            count += 1
            pos = text.find(word, pos + 1)

        return count


word = input('data.txt에서 갯수를 구할 단어를 입력하세요: ')
word = word.lower()

wordCount = countWord('data.txt', word)
print('[%s]의 개수: %d' %(word, wordCount))