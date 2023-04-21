from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://www.lambdatest.com/selenium-playground"


def test_lambdatest_one():
    driver.get(url)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div[1]/ul/li[1]/a").click()
    assert "simple-form-demo" in driver.current_url
    message = "Welcome to LambdaTest"
    driver.find_element(By.ID, "user-message").send_keys(message)
    time.sleep(5)
    driver.find_element(By.ID, "showInput").click()
    time.sleep(5)
    right_hand_panel = driver.find_element(By.ID, "message")
    assert message == right_hand_panel.text


def test_lambdatest_two():
    driver.get(url)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div[2]/ul/li[3]/a").click()
    action = ActionChains(driver)
    drag = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[3]/div/div/div[2]/div[2]/div[1]/div/input")

    action.click_and_hold(drag).move_by_offset(120,0).perform()
    time.sleep(10)


def test_lambdatest_three():
    driver.get(url)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div[1]/ul/li[5]/a").click()
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[3]/div/div/div[2]/div/form/div[6]/button").click()
    name_txtbox = driver.find_element(By.ID, "name")
    assert "Please fill out this field." == name_txtbox.get_attribute("validationMessage")
    driver.find_element(By.ID, "name").send_keys("Abc")
    driver.find_element(By.ID, "inputEmail4").send_keys("abc@xyz.com")
    driver.find_element(By.ID, "inputPassword4").send_keys("pass@123")
    driver.find_element(By.ID, "company").send_keys("pqr")
    driver.find_element(By.ID, "websitename").send_keys("abc.com")
    country = Select(driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[3]/div/div/div[2]/div/form/div[3]/div[1]/select"))
    country.select_by_visible_text("United States")
    time.sleep(5)
    driver.find_element(By.ID, "inputCity").send_keys("New York")
    driver.find_element(By.ID, "inputAddress1").send_keys("new york")
    driver.find_element(By.ID, "inputAddress2").send_keys("abc")
    driver.find_element(By.ID, "inputState").send_keys("Texas")
    driver.find_element(By.ID, "inputZip").send_keys("10001")
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[3]/div/div/div[2]/div/form/div[6]/button").click()
    time.sleep(10)
    output = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[3]/div/div/div[2]/div/p")
    message1 = "Thanks for contacting us, we will get back to you shortly."
    assert message1 == output.text
    driver.close()




