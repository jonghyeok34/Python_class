from bs4 import BeautifulSoup

# 분석하고 싶은 HTML
html = """
<html><body>
<h1 id="title">스크레이핑이란?</h1>
<p id="body">웹 페이지를 분석하는 것</p>
<p id ="other_body">원하는 부분을 추출하는 것</p>
</body></html>
"""


# HTML 분석하기 - BeautifulSoup 인스턴스 생성
# HTML을 분석할 때에는 분석기(parser) 종류를 'html.parser' 라고 지정함
soup = BeautifulSoup(html, 'html.parser')

# 원한느 부분 추출
title = soup.find(id="title")
body = soup.find(id="body")
body2 = soup.find(id="other_body")

# 텍스트출력
print("title = "+title.string)
print("body = "+body.string)
print("body2 = "+body2.string)

