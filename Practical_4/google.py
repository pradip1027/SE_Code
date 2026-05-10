import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()
try:
	browser.get("https://www.google.com")
	print("Page title was '{}'".format(browser.title))
	text = browser.find_element(By.NAME, 'q')
	text.send_keys("iphone")
	print(text.get_attribute("value"))
	text.send_keys(Keys.ENTER)
	time.sleep(30)

finally:
	browser.quit()