# For automating applying for jobs, I'm going to use the 'Brave Browser' and 'Selenium' as the driver
# Selenium is a leading cloud-based testing platform which helps testers record their actions and export them as a reusable script.
# see this resource for an example of web-scraping Indeed: https://www.youtube.com/watch?v=e-3DafD-c4w

from selenium import webdriver
PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Brave(PATH)

driver.get("https://aaronjanovitch.com")
