import numpy as np
import matplotlib.pyplot as plt
import platform
# from PIL import Image
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
from matplotlib import font_manager, rc
# alice.txt 파일과 alice_mask.png 이미지를 읽어와서 변수에 저장함.
text = open('alice.txt').read()
alice_mask = np.array(Image.open('alice_mask.png'))

# alice 소설에서 많이 등장하는 said 라는 단어는 카운트에서 제거함.
stopwords = set(STOPWORDS)
stopwords.add("said")

# matplotlib 에서 한글폰트 설정
path = "c:/Windows/Fonts/malgun.ttf"


if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry')

plt.figure(figsize=(8, 8))
plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()
wc = WordCloud(background_color='white', max_words=2000,
               mask=alice_mask, stopwords=stopwords)
wc = wc.generate(text)
print(wc.words_)

# 앨리스 그림과 wordcloud를 겹쳐서 출력
plt.figure(figsize=(12, 12))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
