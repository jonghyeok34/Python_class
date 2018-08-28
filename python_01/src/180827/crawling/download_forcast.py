import urllib.request
import urllib.parse

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

# forcast.xml 파일로 저장 (w: 쓰기 모드)
with open("forecast.xml", mode="w", encoding="utf-8") as f:
    f.write(text)
    print("저장되었습니다")
