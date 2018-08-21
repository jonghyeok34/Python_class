# 텍스트 파일(data.txt)에서 wordcount를 내림차순으로 출력

# 딕셔너리 = ['단어' :'빈도수']

# 각 단어들의 빈도수를 구해주는 함수

def getTextFreq(filename):
    with open(filename, 'r') as f:
        text = f.read()
        tmp = text.split()
        fa = {}

        for c in tmp:
            if c in fa:
                fa[c] += 1
            else:
                fa[c] = 1

        return fa


freqDict = getTextFreq('data.txt')
print("Dictionary with frequency", freqDict)

sortedFreqDict = sorted(freqDict.items(), key=lambda x: x[1], reverse=True)

# for key, value in 딕셔너리
for word, freq in sortedFreqDict:
    print("[%s] -> %d회" % (word, freq))
