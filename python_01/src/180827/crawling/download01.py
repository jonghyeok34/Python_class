import urllib.request

# URL과 저장 경로 지정하기
# url = "http://uta.pw/shodou/img/28/214.png"
url = "https://t1.daumcdn.net/daumtop_chanel/op/20170315064553027.png"
# savename = "test.png"
savename = "daum.png"

urllib.request.urlretrieve(url, savename)
print("저장 되었습니다.")
