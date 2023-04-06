from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
action = ActionChains(driver)


def test_textbox():
    # load webpage
    driver.get("https://demoqa.com/text-box")
    driver.find_element(By.ID, "userName").send_keys("abc")
    driver.find_element(By.ID, "userEmail").send_keys("xyz@abc.com")
    driver.find_element(By.ID, "currentAddress").send_keys("Mumbai")
    driver.find_element(By.ID, "permanentAddress").send_keys("Bihar")
    submit = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView()",submit)
    submit.click()
    time.sleep(10)
    driver.save_screenshot("textbox.jpeg")