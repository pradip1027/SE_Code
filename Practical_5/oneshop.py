from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time

# 1. Open new driver instance
browser = webdriver.Edge()

try:
    browser.get("https://shop.one-shore.com/index.php")

    '''search_box = browser.find_element(By.CLASS_NAME,"ui-autocomplete-input")
    search_box.send_keys("mug")
    time.sleep(3)

    btn = browser.find_element(By.TAG_NAME,"button")
    btn.click()
    time.sleep(1)'''

    all_products = browser.find_element(By.XPATH, '//*[@id="content"]/section/a')
    all_products.click()
    time.sleep(5)

    product_lists = browser.find_elements(By.CLASS_NAME, "product-description")
    print("no of products:", len(product_lists))

    '''items = browser.find_elements(By.CLASS_NAME, "product-description")

    print("\nTotal Products Found:", len(items))'''
    print("-----------------------------------")

    for product in product_lists:
        title = product.find_element(By.CLASS_NAME, "product-title").text
        price = product.find_element(By.CLASS_NAME, "price").text
        print("Product Name:", title)
        print("Price:", price)
        print("-----------------------------------")

    time.sleep(5)


finally:
    browser.quit()
