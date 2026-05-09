import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

browser = webdriver.Chrome()
test_file_path = os.path.abspath(__file__)
browser.get("C:\\Users\\pradi\\OneDrive\\Documents\\ICT\\Sem_4\\SE\\SE_Code\\Exam\\Internal_Practical\\Job Application Form_Batch 45.html")

def empty_field():
    case_ans = False

    apply_btn = browser.find_element(By.XPATH,"/html/body/form/button")
    apply_btn.click()

    error_occured = browser.find_elements(By.TAG_NAME,"div")

    if(len(error_occured) > 0):
        case_ans = True
    else:
        case_ans = False
    return case_ans
    

def invalid_name():
    case_ans = False

    name = browser.find_element(By.XPATH,"/html/body/form/input[1]")
    name.send_keys("Pradip123")

    exp = browser.find_element(By.XPATH,"/html/body/form/input[2]")
    exp.send_keys("10")

    salary = browser.find_element(By.XPATH,"/html/body/form/input[3]")
    salary.send_keys("10000")

    skill1 = browser.find_element(By.XPATH,"/html/body/form/input[4]")
    skill1.click()

    skill2 = browser.find_element(By.XPATH,"/html/body/form/input[6]")
    skill2.click()

    file_upload = browser.find_element(By.XPATH,"/html/body/form/input[8]")
    file_upload.send_keys(test_file_path)

    apply_btn = browser.find_element(By.XPATH,"/html/body/form/button")
    apply_btn.click()

    error_occured = browser.find_elements(By.TAG_NAME,"div")

    if(len(error_occured) > 0):
        case_ans = True
    else:
        case_ans = False
    return case_ans

def exp_range():
    case_ans = True

    name = browser.find_element(By.XPATH,"/html/body/form/input[1]")
    name.send_keys("Pradip")

    exp = browser.find_element(By.XPATH,"/html/body/form/input[2]")
    exp.send_keys("25")

    salary = browser.find_element(By.XPATH,"/html/body/form/input[3]")
    salary.send_keys("10000")

    skill1 = browser.find_element(By.XPATH,"/html/body/form/input[4]")
    skill1.click()

    skill2 = browser.find_element(By.XPATH,"/html/body/form/input[6]")
    skill2.click()

    file_upload = browser.find_element(By.XPATH,"/html/body/form/input[8]")
    file_upload.send_keys(test_file_path)

    apply_btn = browser.find_element(By.XPATH,"/html/body/form/button")
    apply_btn.click()

    error_occured = browser.find_elements(By.TAG_NAME,"div")

    if(len(error_occured) > 0):
        case_ans = True
    else:
        case_ans = False
    return case_ans
    

def min_salary():
    case_ans = True

    name = browser.find_element(By.XPATH,"/html/body/form/input[1]")
    name.send_keys("Pradip")

    exp = browser.find_element(By.XPATH,"/html/body/form/input[2]")
    exp.send_keys("25")

    salary = browser.find_element(By.XPATH,"/html/body/form/input[3]")
    salary.send_keys("5000")

    skill1 = browser.find_element(By.XPATH,"/html/body/form/input[4]")
    skill1.click()

    skill2 = browser.find_element(By.XPATH,"/html/body/form/input[6]")
    skill2.click()

    file_upload = browser.find_element(By.XPATH,"/html/body/form/input[8]")
    file_upload.send_keys(test_file_path)

    apply_btn = browser.find_element(By.XPATH,"/html/body/form/button")
    apply_btn.click()

    error_occured = browser.find_elements(By.TAG_NAME,"div")

    if(len(error_occured) > 0):
        case_ans = True
    else:
        case_ans = False
    return case_ans

def one_skill():
    case_ans = True

    name = browser.find_element(By.XPATH,"/html/body/form/input[1]")
    name.send_keys("Pradip")

    exp = browser.find_element(By.XPATH,"/html/body/form/input[2]")
    exp.send_keys("25")

    salary = browser.find_element(By.XPATH,"/html/body/form/input[3]")
    salary.send_keys("5000")

    skill1 = browser.find_element(By.XPATH,"/html/body/form/input[4]")
    skill1.click()

    # skill2 = browser.find_element(By.XPATH,"/html/body/form/input[6]")
    # skill2.click()

    file_upload = browser.find_element(By.XPATH,"/html/body/form/input[8]")
    file_upload.send_keys(test_file_path)

    apply_btn = browser.find_element(By.XPATH,"/html/body/form/button")
    apply_btn.click()

    error_occured = browser.find_elements(By.TAG_NAME,"div")

    if(len(error_occured) > 0):
        case_ans = True
    else:
        case_ans = False
    return case_ans
    

class htmltestcases(unittest.TestCase):
    def test_empty_field(self):
        result = empty_field()
        self.assertTrue(result)
    
    def test_invalid_name(self):
        result = invalid_name()
        self.assertTrue(result)
    
    def test_exp_range(self):
        result = exp_range()
        self.assertTrue(result)
    
    def test_min_salary(self):
        result = min_salary()
        self.assertTrue(result)
    
    def test_one_skill(self):
        result = one_skill()
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()