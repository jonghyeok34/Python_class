import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# 매개변수를 URL 인코딩

values = {
    'stnId': 108
}
params = urllib.parse.urlencode(values)

# 요청 전용 URL 생성
url = API + "?" + params
# url = API +"?stnId=108"
print("url=" + url)

# xml파일을 읽어와서 출력
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)


# HTML 분석하기 - BeautifulSoup 인스턴스 생성
# HTML을 분석할 때에는 분석기(parser) 종류를 'html.parser' 라고 지정함
soup = BeautifulSoup(text, 'html.parser')

# 원하는 부분 추출
cities = soup.find_all("city")
for city in cities:
    print(city.string)
