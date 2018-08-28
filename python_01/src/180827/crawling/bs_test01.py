from bs4 import BeautifulSoup

# 분석하고 싶은 HTML
html = """
<html><body>
<h1>스크레이핑이란?</h1>
<p>웹 페이지를 분석하는 것</p>
<p>원하는 부분을 추출하는 것</p>
<p>원하는 부분을 추출하는 것2</p>
</body></html>
"""

# HTML 분석하기 - BeautifulSoup 인스턴스 생성
# HTML을 분석할 때에는 분석기(parser) 종류를 'html.parser' 라고 지정함
soup = BeautifulSoup(html, 'html.parser')

# 원한느 부분 추출
h1 = soup.html.body.h1
p1 = soup.html.body.p

# p1.next_sibling 에서는 </p> 뒤에 있는 줄바꿈 또는 공백이 추출됨
# next_sibling 을 한번 더 사용해 2번째 <p>태그를 추출합니다.
p2 = p1.next_sibling.next_sibling
p3 = p2.next_sibling.next_sibling

# 요소의 글자 출력하기 : string속성으로 요소 사이의 글자 부분을 추출함
print("h1 = "+h1.string)
print("p1 = "+p1.string)
print("p2 = "+p2.string)
print("p3 = "+p3.string)
