import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



#launching browser
browser = webdriver.Edge()

try:
    # opening Browser stack using get method
    # browser.get("https://the-internet.herokuapp.com/login")
    # print("Page Opened was '{}'".format(browser.title))

    browser.get("https://www.browserstack.com/users/sign_up")

    time.sleep(30)
    # sign_in_txt = browser.find_element(By.CLASS_NAME,' bstack-mm-link bstack-mm-main-link-sign-in ')
    # sign_in_txt.click()

    full_name = browser.find_element(By.XPATH,"//*[@id='user_full_name']")
    full_name.send_keys("Pradip Parmar")
    time.sleep(2)

    # name = browser.find_element(By.ID,'user_full_name')
    # name.send_keys("Pradip Parmar")

    email = browser.find_element(By.XPATH,"//*[@id='user_email_login']")
    email.send_keys("24162581027@gnu.ac.in")
    time.sleep(4)

    # email = browser.find_element(By.ID,'username')
    # email.send_keys("tomsmith")
    # time.sleep(5)

    passwd = browser.find_element(By.XPATH,"//*[@id='user_password']")
    passwd.send_keys("guniict@2024")
    time.sleep(1)
    
    # email = browser.find_element(By.ID,'user_email_login')
    # email.send_keys("24162581027@gnu.ac.in")
    # time.sleep(5)

    check_box = browser.find_element(By.XPATH,"//*[@id='tnc_checkbox']")
    check_box.click()
    time.sleep(5)

    # pswd = browser.find_element(By.ID,'password')
    # pswd.send_keys("SuperSecretPassword!")
    # time.sleep(5)

    # pswd = browser.find_element(By.ID,'user_password')
    # pswd.send_keys("guniict@2024")
    # time.sleep(5)

    sign_up_btn = browser.find_element(By.XPATH,"//*[@id='user_submit']")
    sign_up_btn.click()
    time.sleep(20)

    # check = browser.find_element(By.ID,'tnc_checkbox')
    # check.click()

    # login = browser.find_element(By.CLASS_NAME,'radius')
    # login.click()

    # login = browser.find_element(By.ID,'user_submit')
    # login.click()


    # time.sleep(30)

finally:
    browser.quit()