from bs4 import BeautifulSoup

# 분석하고 싶은 HTML
html = """
<html><body>
<ul>
<li><a href="http://www.naver.com">naver</a></li>
<li><a href="http://www.daum.net">daum</a></li>
</ul>
</body></html>
"""

# HTML 분석하기 - BeautifulSoup 인스턴스 생성
# HTML을 분석할 때에는 분석기(parser) 종류를 'html.parser' 라고 지정함
soup = BeautifulSoup(html, 'html.parser')

# 원하는 부분 추출
links = soup.find_all("a")

# 링크 목록 출력
for a in links:
    href = a.attrs['href']
    text = a.string
    print(text, ">", href)
