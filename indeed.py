import os
from os.path import join, dirname
from dotenv import load_dotenv
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
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
driver = webdriver.Chrome(options=browser_options, executable_path=PATH)

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
