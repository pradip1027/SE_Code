import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://www.browserstack.com/users/sign_up")
time.sleep(10)

def signup_page_title():
    case_ans = True
    actual_title = browser.title
    # Intentionally checking for wrong title to make this test fail
    if "Google" in actual_title:
        case_ans = True
    else:
        case_ans = False
    return case_ans

def full_name_field_validation():
    case_ans = True
    full_name = browser.find_element(By.ID, "user_full_name")
    full_name.clear()
    full_name.send_keys("Pradip")
    if full_name.get_attribute("value") == "Pradip":
        case_ans = True
    else:
        case_ans = False
    return case_ans

def email_field_validation():
    case_ans = True
    email = browser.find_element(By.ID, "user_email_login")
    email.clear()
    email.send_keys("24162581027@gnu.ac.in")
    if email.get_attribute("value") == "24162581027@gnu.ac.in":
        case_ans = True
    else:
        case_ans = False
    return case_ans

def password_field_validation():
    case_ans = True
    password = browser.find_element(By.ID, "user_password")
    password.clear()
    password.send_keys("guniict@2024")
    if password.get_attribute("value") == "guniict@2024":
        case_ans = True
    else:
        case_ans = False
    return case_ans

def terms_checkbox_validation():
    case_ans = True
    checkbox = browser.find_element(By.ID, "tnc_checkbox")
    if not checkbox.is_selected():
        checkbox.click()
    if checkbox.is_selected():
        case_ans = True
    else:
        case_ans = False
    return case_ans

def signup_button_validation():
    case_ans = True
    submit_btn = browser.find_element(By.ID, "user_submit")
    if submit_btn.is_displayed() and submit_btn.is_enabled():
        case_ans = True
    else:
        case_ans = False
    return case_ans

def empty_form_submission():
    case_ans = True
    # Clear all fields first
    browser.find_element(By.ID, "user_full_name").clear()
    browser.find_element(By.ID, "user_email_login").clear()
    browser.find_element(By.ID, "user_password").clear()

    submit_btn = browser.find_element(By.ID, "user_submit")
    submit_btn.click()
    time.sleep(10)

    if "sign_up" in browser.current_url:
        case_ans = True
    else:
        case_ans = False
    return case_ans

def signup_page_url():
    case_ans = True
    current_url = browser.current_url
    # Intentionally checking for wrong URL to make this test fail
    if "browserstack.com/users/login" in current_url:
        case_ans = True
    else:
        case_ans = False
    return case_ans


class TestBrowserStackSignUp(unittest.TestCase):
    def test_signup_page_title(self):
        result = signup_page_title()
        self.assertTrue(result, "FAILED: Page title does not contain 'Google' - expected 'Google' in title but got BrowserStack page title")

    def test_full_name_field_validation(self):
        result = full_name_field_validation()
        self.assertTrue(result, "FAILED: Full Name field did not accept input correctly")

    def test_email_field_validation(self):
        result = email_field_validation()
        self.assertTrue(result, "FAILED: Email field did not accept input correctly")

    def test_password_field_validation(self):
        result = password_field_validation()
        self.assertTrue(result, "FAILED: Password field did not accept input correctly")

    def test_terms_checkbox_validation(self):
        result = terms_checkbox_validation()
        self.assertTrue(result, "FAILED: Terms checkbox could not be checked")

    def test_signup_button_validation(self):
        result = signup_button_validation()
        self.assertTrue(result, "FAILED: Sign Up button is not displayed or not enabled")

    def test_empty_form_submission(self):
        result = empty_form_submission()
        self.assertTrue(result, "FAILED: Empty form submission redirected away from sign_up page")

    def test_signup_page_url(self):
        result = signup_page_url()
        self.assertTrue(result, "FAILED: Current URL does not contain 'browserstack.com/users/login' - page is on sign_up not login")

if __name__ == "__main__":
    unittest.main()