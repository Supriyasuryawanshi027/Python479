from selenium import webdriver

CHROME_DRIVER_PATH = 'D:\\pythonProject\\selenium_automation\\drivers\\chromedriver.exe'
#APP_PATH = 'https://demoqa.com/alerts'
APP_PATH = 'https://opensource-demo.orangehrmlive.com/'
from selenium.webdriver.common.alert import Alert

print('Step 1: Launch the browser')
driver = webdriver.Chrome(executable_path = CHROME_DRIVER_PATH)
driver.get(APP_PATH)
driver.implicitly_wait(20)
driver.find_element_by_id('btnLogin').click()

import time
time.sleep(30)

driver.find_element_by_id('alertButton')
alert = Alert(driver)




driver.find_element_by_id('confirmButton').click()
alert = Alert(driver)
alert.accept()