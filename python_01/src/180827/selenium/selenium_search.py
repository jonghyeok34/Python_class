from selenium import webdriver

path = "c:/downloads/chromedriver.exe"

# selenium의 webdriver로 크롬 브라우저를 실행
driver = webdriver.Chrome(path)

# google에 접속한다
driver.get("http://www.google.co.kr")

# 검색 입력 부분에 커서를 올리고 검색 입력 부분에 다양한 명령을 내리기 위해
# elem 변수에 할당
elem = driver.find_element_by_name("q")

elem.clear()

elem.send_keys("Selenium")

elem.submit()