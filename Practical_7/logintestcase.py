import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# Get the path to the login1.html file
html_file_path = os.path.join(os.path.dirname(__file__), "login1.html")
file_url = "file:///" + html_file_path.replace("\\", "/")

browser = webdriver.Chrome()
browser.get(file_url)
time.sleep(5)

def empty_username_and_password():
    case_ans = True
    username = browser.find_element(By.ID, "username")
    password = browser.find_element(By.ID, "password")
    usernameError = browser.find_element(By.ID, "usernameError")
    
    username.clear()
    password.clear()
    
    submit_btn = browser.find_element(By.TAG_NAME, "button")
    submit_btn.click()
    time.sleep(2)
    
    if "Username cannot be empty" in usernameError.text:
        case_ans = True
    else:
        case_ans = False
    return case_ans

def username_with_digits():
    case_ans = True
    username = browser.find_element(By.ID, "username")
    password = browser.find_element(By.ID, "password")
    usernameError = browser.find_element(By.ID, "usernameError")
    
    username.clear()
    username.send_keys("123")
    password.clear()
    password.send_keys("Test@123")
    
    submit_btn = browser.find_element(By.TAG_NAME, "button")
    submit_btn.click()
    time.sleep(2)
    
    if "Username cannot contain digits or special symbols" in usernameError.text:
        case_ans = True
    else:
        case_ans = False
    return case_ans

def username_too_short():
    case_ans = True
    username = browser.find_element(By.ID, "username")
    password = browser.find_element(By.ID, "password")
    usernameError = browser.find_element(By.ID, "usernameError")
    
    username.clear()
    username.send_keys("ab")
    password.clear()
    password.send_keys("Test@123")
    
    submit_btn = browser.find_element(By.TAG_NAME, "button")
    submit_btn.click()
    time.sleep(2)
    
    if "Username must be at least 3 characters long" in usernameError.text:
        case_ans = True
    else:
        case_ans = False
    return case_ans

def username_with_special_symbols():
    case_ans = True
    username = browser.find_element(By.ID, "username")
    password = browser.find_element(By.ID, "password")
    usernameError = browser.find_element(By.ID, "usernameError")
    
    username.clear()
    username.send_keys("ab@ab")
    password.clear()
    password.send_keys("Test@123")
    
    submit_btn = browser.find_element(By.TAG_NAME, "button")
    submit_btn.click()
    time.sleep(2)
    
    if "Username cannot contain digits or special symbols" in usernameError.text:
        case_ans = True
    else:
        case_ans = False
    return case_ans

def login_successful():
    case_ans = True
    username = browser.find_element(By.ID, "username")
    password = browser.find_element(By.ID, "password")
    successElement = browser.find_element(By.ID, "success")
    
    username.clear()
    username.send_keys("tt")
    password.clear()
    password.send_keys("Test@123")
    
    submit_btn = browser.find_element(By.TAG_NAME, "button")
    submit_btn.click()
    time.sleep(2)
    
    if "Login successful" in successElement.text:
        case_ans = True
    else:
        case_ans = False
    return case_ans

def password_too_short():
    case_ans = True
    username = browser.find_element(By.ID, "username")
    password = browser.find_element(By.ID, "password")
    passwordError = browser.find_element(By.ID, "passwordError")
    
    username.clear()
    username.send_keys("test")
    password.clear()
    password.send_keys("12")
    
    submit_btn = browser.find_element(By.TAG_NAME, "button")
    submit_btn.click()
    time.sleep(2)
    
    if "Password must be at least 6 characters long" in passwordError.text:
        case_ans = True
    else:
        case_ans = False
    return case_ans

def password_without_uppercase():
    case_ans = True
    username = browser.find_element(By.ID, "username")
    password = browser.find_element(By.ID, "password")
    passwordError = browser.find_element(By.ID, "passwordError")
    
    username.clear()
    username.send_keys("test")
    password.clear()
    password.send_keys("123456")
    
    submit_btn = browser.find_element(By.TAG_NAME, "button")
    submit_btn.click()
    time.sleep(2)
    
    if "Password must contain at least one uppercase letter" in passwordError.text:
        case_ans = True
    else:
        case_ans = False
    return case_ans

def password_without_special_character():
    case_ans = True
    username = browser.find_element(By.ID, "username")
    password = browser.find_element(By.ID, "password")
    passwordError = browser.find_element(By.ID, "passwordError")
    
    username.clear()
    username.send_keys("test")
    password.clear()
    password.send_keys("Abc123456")
    
    submit_btn = browser.find_element(By.TAG_NAME, "button")
    submit_btn.click()
    time.sleep(2)
    
    if "Password must contain at least one special character (@$!%*?&)" in passwordError.text:
        case_ans = True
    else:
        case_ans = False
    return case_ans

def invalid_password_attempt():
    case_ans = True
    username = browser.find_element(By.ID, "username")
    password = browser.find_element(By.ID, "password")
    errorElement = browser.find_element(By.ID, "error")
    
    username.clear()
    username.send_keys("test")
    password.clear()
    password.send_keys("Abc@123456")
    
    submit_btn = browser.find_element(By.TAG_NAME, "button")
    submit_btn.click()
    time.sleep(2)
    
    if "Invalid username or password" in errorElement.text:
        case_ans = True
    else:
        case_ans = False
    return case_ans


class TestLoginForm(unittest.TestCase):
    def test_1_empty_username_and_password(self):
        result = empty_username_and_password()
        self.assertTrue(result, "FAILED: Empty username and password validation - expected 'Username cannot be empty'")

    def test_2_username_with_digits(self):
        result = username_with_digits()
        self.assertTrue(result, "FAILED: Username with digits validation - expected 'Username cannot contain digits or special symbols'")

    def test_3_username_too_short(self):
        result = username_too_short()
        self.assertTrue(result, "FAILED: Username too short validation - expected 'Username must be at least 3 characters long'")

    def test_4_username_with_special_symbols(self):
        result = username_with_special_symbols()
        self.assertTrue(result, "FAILED: Username with special symbols validation - expected 'Username cannot contain digits or special symbols'")

    def test_5_login_successful(self):
        result = login_successful()
        self.assertTrue(result, "FAILED: Login successful test - expected 'Login successful'")

    def test_6_password_too_short(self):
        result = password_too_short()
        self.assertTrue(result, "FAILED: Password too short validation - expected 'Password must be at least 6 characters long'")

    def test_7_password_without_uppercase(self):
        result = password_without_uppercase()
        self.assertTrue(result, "FAILED: Password without uppercase validation - expected 'Password must contain at least one uppercase letter'")

    def test_8_password_without_special_character(self):
        result = password_without_special_character()
        self.assertTrue(result, "FAILED: Password without special character validation - expected 'Password must contain at least one special character (@$!%*?&)'")

    def test_9_invalid_password_attempt(self):
        result = invalid_password_attempt()
        self.assertTrue(result, "FAILED: Invalid password attempt - expected 'Invalid username or password'")


if __name__ == '__main__':
    unittest.main()
