import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.maximize_window()
action = ActionChains(driver)


@pytest.mark.skip
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


# find checkbox
@pytest.mark.skip
def test_chkbox():
    url = "https://the-internet.herokuapp.com/checkboxes"
    driver.get(url)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/input[1]").click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/input[2]").click()
    time.sleep(5)
    driver.save_screenshot("txtbox.jpg")


@pytest.mark.skip
def test_login():
    driver.get("https://www.facebook.com/login.php")
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[1]/input").send_keys("abc")
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[2]/div/div/input").send_keys("xyz")
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[3]/button").click()
    time.sleep(10)


@pytest.mark.skip
def test_context_menu():
    driver.get("https://the-internet.herokuapp.com/context_menu")
    right_click = driver.find_element(By.ID, "hot-spot")
    action.context_click(right_click).perform()
    time.sleep(5)
    alert = Alert(driver)
    alert.accept()
    time.sleep(5)

@pytest.mark.skip
def test_alert_IO():
    driver.get("https://the-internet.herokuapp.com/")
    driver.find_element(By.PARTIAL_LINK_TEXT, "Digest").click()
    alerts = driver.switch_to.alert
    alerts.send_keys("abc")
    alerts.send_keys(Keys.TAB)
    alerts.send_keys("xyz")
    time.sleep(5)
    alerts.accept()
    time.sleep(5)


def test_drag_drop():
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")
    ele1 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]")
    ele2 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]")
    action = ActionChains(driver)
    action.drag_and_drop(ele1,ele2)

    action.perform()
    time.sleep(5)
    # driver.save_screenshot("dragdrop.jpg")


@pytest.mark.skip
def test_dropdown():
    driver.get("https://the-internet.herokuapp.com/dropdown")
    dropdown = Select(driver.find_element(By.ID, "dropdown"))
    dropdown.select_by_index(1)
    time.sleep(2)
    driver.save_screenshot("dropdown.png")


def test_dynamic_content():
    driver.get("https://the-internet.herokuapp.com/dynamic_content")
    driver.find_element(By.XPATH, "//*[@id="'content'"]/div[1]/div[2]")
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div[2]")
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[3]/div[2]")
    time.sleep(10)








