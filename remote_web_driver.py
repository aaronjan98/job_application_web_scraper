import os
from os.path import join, dirname
from dotenv import load_dotenv
from multiprocessing import Process
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
indeed_email = os.getenv('INDEED_EMAIL')
indeed_password = os.getenv('INDEED_PASSWORD')

# The main process calls this function to create the driver instance.
def createDriverInstance():
    PATH = '/usr/local/bin/chromedriver'
    browser_options = Options()
    browser_options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
    browser_options.add_argument('start-maximized')
    browser_options.add_argument('--disable-infobars')
    driver = webdriver.Chrome(options=browser_options, executable_path=PATH)
    return driver

# Called by the second process only.
# executor_url:  http://127.0.0.1:57124
# session_id:  698666c381b2d5afcb712aac00fad56d
def secondProcess(executor_url, session_id):
    options = Options()
    options.add_argument("--disable-infobars")
    options.add_argument("--enable-file-cookies")
    capabilities = options.to_capabilities()
    same_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities=capabilities)
    same_driver.close()
    same_driver.command_executor._url = executor_url
    same_driver.session_id = session_id
    print('executor_url: ', executor_url)
    print('session_id: ', session_id)
    same_driver.get("https://www.indeed.com")
    time.sleep(30)
    same_driver.quit()

if __name__ == '__main__':
    driver = createDriverInstance()
    driver.get("https://www.indeed.com")
    time.sleep(30)

    # Pass the driver session and command_executor to the second process.
    p = Process(target=secondProcess, args=(driver.command_executor._url, driver.session_id))
    # p = Process(target=secondProcess, args=('http://127.0.0.1:57124', '698666c381b2d5afcb712aac00fad56d'))
    p.start()
