import requests

r = requests.get("http://wikibook.co.kr/wikibook.png")

# 바이너리 형식으로 데이터 저장(w: 쓰기, b:바이너리)
with open("test.png", "wb") as f:
    f.write(r.content)
print("saved")
