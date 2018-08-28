from selenium import webdriver

path = "c:/downloads/chromedriver.exe"
driver = webdriver.Chrome(path)

# 3초 대기하기
driver.implicitly_wait(3)

# URL 읽어 들이기
driver.get("https://www.nate.com")

# 화면을 캡처해서 저장하기
driver.save_screenshot("website.png")

# 브라우저 종료하기
driver.quit()
