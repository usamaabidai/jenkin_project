import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
import time
import allure


def setup_function():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    time.sleep(2)

def teardown_function():
    driver.quit()

def my_cred():
    return [('standard_user', 'secret_sauces'), ('locked_out_users', 'secret_sauce'), ('performance_glitch_users', 'secret_sauce')]

@pytest.mark.parametrize("username, password", my_cred())
def test_login(username, password):
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    # Capture a screenshot and attach it to the Allure report
    allure.attach(driver.get_screenshot_as_png(), name="myalnafi_sc", attachment_type=AttachmentType.PNG)
