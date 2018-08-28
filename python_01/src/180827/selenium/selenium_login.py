from selenium import webdriver

USER = "abc960620"  # naver.com userid 설정
PASS = "spdlqjq12!"  # naver.com password 설정

browser = webdriver.Chrome("c:/downloads/chromedriver.exe")
browser.implicitly_wait(3)

# 로그인 페이지에 접근하기
browser.get("https://nid.naver.com/nidlogin.login")
print("로그인 페이지에 접근합니다.")

# 텍스트 박스에 아이디와 비밀번호 입력하기(회원인증)
e = browser.find_element_by_name("id")
e.clear()
e.send_keys(USER)

e = browser.find_element_by_name("pw")
e.clear()
e.send_keys(PASS)

# 입력 양식 전송해서 로그인

form = browser.find_element_by_css_selector("input.btn_global[type=submit]")
form.submit()
print("로그인 버튼을 클릭합니다.")

# 쇼핑 페이지의 데이터 가져오기
browser.get("https://order.pay.naver.com/home?tabMenu=SHOPPING")

# 쇼핑 목록 출력하기
products = browser.find_elements_by_css_selector(".p_info span")
print(products)
for product in products:
    print("-", product.text)
