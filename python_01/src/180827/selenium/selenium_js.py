from selenium import webdriver

path = "c:/downloads/chromedriver.exe"

driver = webdriver.Chrome(path)

driver.implicitly_wait(3)

driver.get("https://www.google.com")

r = driver.execute_script("return 100 + 50")
print(r)