from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

PATH = "/usr/local/bin/chromedriver"
browser_options = Options()
browser_options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
browser_options.add_argument("start-maximized")

driver = webdriver.Chrome(options=browser_options, executable_path=PATH)

driver.get("https://aaronjanovitch.com")
print(driver.title)

time.sleep(5)

driver.quit()
