# json 데이터 읽어오기

import urllib.request as req
import os.path
import json

# json 데이터 다운로드
url = "https://api.github.com/repositories"
savename = "repo.json"

if not os.path.exists(url):
    req.urlretrieve(url, savename)

# repo.json 값 읽어오기
items = json.load(open(savename, 'r', encoding='utf-8'))
print(items)

# 특정 정보(name, login) 출력
for item in items:
    print("{0} : {1}"
          .format(item['name'], item['owner']['login']))
