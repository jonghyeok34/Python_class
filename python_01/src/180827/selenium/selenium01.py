# selenium 모듈에서 webdriver를 불러온다
from selenium import webdriver

# 다운로드 받아 압축을 해제한 driver 파일 경로를 path 변수에 할당한다
path = "c:/downloads/chromedriver.exe"

# 조금만 기다리면 selenium으로 제어할 수 있는 브라우저 새창이 뜬다
driver = webdriver.Chrome(path)

# webdriver가 google 페이지에 접속하도록 명령
driver.get('https://www.google.com')