import os
from os.path import join, dirname
from dotenv import load_dotenv
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Retrieving login information from .env
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Accessing variables.
email = os.getenv('INDEED_EMAIL')
password = os.getenv('INDEED_PASSWORD')

# Setting up Browser configurations
PATH = "/usr/local/bin/chromedriver"
browser_options = Options()
browser_options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
browser_options.add_argument("start-maximized")
# what are experimental options?
# browser_options.add_experimental_option(name, value)
driver = webdriver.Chrome(options=browser_options, executable_path=PATH)

# executor_url = driver.command_executor._url
# session_id = driver.session_id
executor_url = driver.command_executor._url
session_id = driver.session_id
print('Executor URL: ', executor_url)
print('session ID: ', session_id)
driver.get("https://www.indeed.com")

# start another browser by using existing webdriver and replace new session_id by existing one. That helps to connect to existing Selenium Webdriver session.
driver2 = webdriver.Remote(command_executor=executor_url)
driver2.session_id = session_id
print (driver2.current_url)

'''
def attach_to_session(executor_url, session_id):
    original_execute = WebDriver.execute
    def new_command_execute(self, command, params=None):
        if command == "newSession":
            # Mock the response
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return original_execute(self, command, params)
    # Patch the function before creating the driver object
    WebDriver.execute = new_command_execute
    driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    driver.session_id = session_id
    # Replace the patched function with original function
    WebDriver.execute = original_execute
    return driver

bro = attach_to_session('http://127.0.0.1:64092', '8de24f3bfbec01ba0d82a7946df1d1c3')
bro.get('http://ya.ru/')
'''
'''
driver.get("https://www.indeed.com")

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Sign in"))
    ).click()
except:
    driver.quit()

# Sign in
# driver.find_element_by_link_text("Sign in").click()

# check if this element exists first
# email_input = driver.find_element_by_id("login-email-input")

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login-email-input"))
    ).send_keys(email)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login-password-input"))
    ).send_keys(password)
    # check for captcha
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "checkbox"))
    ).click()
    # WebDriverWait(driver, 10).until(
        # EC.presence_of_element_located((By.ID, "login-submit-button"))
    # ).send_keys(Keys.RETURN)
except:
    driver.quit()

# time.sleep(5)
# driver.quit()
'''
