import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



#launching browser
browser = webdriver.Edge()

try:
    browser.get("https://shop.one-shore.com/index.php")

    sign_in_option = browser.find_element(By.ID,"_desktop_user_info")
    sign_in_option.click()
    time.sleep(2)

    email = browser.find_element(By.NAME,"email")
    email.send_keys("24162581027@gnu.ac.in")
    time.sleep(3)

    passwd = browser.find_element(By.NAME,"password")
    passwd.send_keys("guniict@2024")
    time.sleep(1)

    sign_in_btn = browser.find_element(By.ID,"submit-login")
    sign_in_btn.click()
    time.sleep(5)

    browser.get("https://shop.one-shore.com/index.php?id_category=6&controller=category")
    img_click = browser.find_element(By.XPATH,"//img[@alt='Mug The best is yet to come']")
    img_click.click()
    time.sleep(5)

    # item_increase = browser.find_element(By.CLASS_NAME,"material-icons touchspin-up")
    # item_increase.click()
    # item_increase.click()
    # time.sleep(1)

    add_to_cart = browser.find_element(By.XPATH,"//*[@id='add-to-cart-or-refresh']/div[2]/div/div[2]/button")
    add_to_cart.click()
    time.sleep(5)

    check_out = browser.find_element(By.XPATH,"//*[@id='blockcart-modal']/div/div/div[2]/div/div[2]/div/div/a")
    check_out.click()
    time.sleep(3)

    check_out = browser.find_element(By.XPATH,"//*[@id='main']/div/div[1]/div/div[2]/ul/li/div/div[3]/div/div[3]/div/a/i")
    check_out.click()
    time.sleep(3)

finally:
    browser.quit()