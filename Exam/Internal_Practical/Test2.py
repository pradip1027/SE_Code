from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///C:/Users/pradi/Downloads/Online%20Course%20Enrollment%20Form_Batch%2043.html")
time.sleep(2)

name_error = ""
age_error = ""
driver.find_element(By.XPATH, "//*[@id='name']").send_keys("")
driver.find_element(By.XPATH, "//*[@id='email']").send_keys("")
driver.find_element(By.XPATH, "//*[@id='course']/option[2]").click()
driver.find_element(By.XPATH, "//*[@id='age']").send_keys("93")

submit_button = driver.find_element(By.XPATH, "/html/body/form/button")
submit_button.click()

for element in driver.find_elements(By.XPATH, "//*[@id='nameError']"):
    if element.is_displayed():
        name_error = element.text
        break
 
for element in driver.find_elements(By.XPATH, "//*[@id='ageError']"):
    if element.is_displayed():
        age_error = element.text
        break   

for element in driver.find_elements(By.XPATH, "//*[@id='emailError']"):   
    if element.is_displayed():
        email_error=element.text
        break

print("Validation Errors:")
if not name_error and not age_error:
    print("No validation errors found.")

print("Name Error:", name_error)
print("Age Error:", age_error)
print("Email:",email_error)



time.sleep(5)
driver.quit()