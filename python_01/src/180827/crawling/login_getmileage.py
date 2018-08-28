# import requests
# from bs4 import BeautifulSoup
#
# # 아이디와 비밀번호 지정하기[자신의 것을 사용]
# USER = "guardian23"
# PASS = ""
#
# # 세션 시작하기
# session = requests.session()
#
# # 파이썬 프로그램으로 로그인
# login_info = {
#     "m_id": USER,  # 아이디 지정
#     "m_password": PASS  # 비밀번호 지정
# }
# url_login = "http://www.hanbit.co.kr/member/login_proc.php"
# res = session.post(url_login, data=login_info)  # URL에 post요청 수행
#
# url_mypage = "http://www.hanbit.co.kr/myhanbit/myhanbit.html"
# res = session.get(url_mypage)
#
# # BeautifulSoup 인스턴스 생성
# soup = BeautifulSoup(res.text, "html.parser")
#
# # 마일리지와 이코인 가져오기
# mileage = soup.select_one(".mileage_section1 span").get_text()
# ecoin = soup.select_one(".mileage_section2 span").get_text()
# print("마일리지: " + mileage)
# print("이코인: " + ecoin)

import requests
from bs4 import BeautifulSoup

# 아이디와 비밀번호 지정하기[자신의 것을 사용]
USER = "abc960620"
PASS = "비밀번호"
# 세션 시작하기
session = requests.session()

# 파이썬 프로그램으로 로그인하기
login_info = {
    "m_id": USER,  # 아이디 지정
    "m_passwd": PASS  # 비밀번호 지정
}

url_login = "http://www.hanbit.co.kr/member/login_proc.php"
res = session.post(url_login, data=login_info)  # URL에 post 요청을 수행

# 로그인이 완료되면 마이페이지에 접근
url_mypage = "http://www.hanbit.co.kr/myhanbit/myhanbit.html"
res = session.get(url_mypage)

# BeautifulSoup 인스턴스 생성하기 - 텍스트 형식으로 데이터 추출
soup = BeautifulSoup(res.text, "html.parser")

test = soup.select("span")
for text in test:
    print(text.text)


# 마일리지와 이코인 가져오기
mileage = soup.select_one(".mileage_section1 span").string
ecoin = soup.select_one(".mileage_section2 span")
print("마일리지: " + mileage)
print("이코인: " + ecoin)
