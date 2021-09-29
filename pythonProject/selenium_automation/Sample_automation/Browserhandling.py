import time
from selenium import webdriver

CHROME_DRIVER_PATH = 'D:\\pythonProject\\selenium_automation\\drivers\\chromedriver.exe'
APPLICATION_URL = 'https://opensource-demo.orangehrmlive.com/'

print('Step1 : Launch the browser ')
driver = webdriver.Chrome(executable_path = CHROME_DRIVER_PATH)

print('Step2 : Enter Url into Address Bar')
driver.get(APPLICATION_URL)

import time
driver.minimize_window()
time.sleep(2)

driver.maximize_window()
time.sleep(2)

driver.fullscreen_window()
print('Step 3 : Find the Username Input Box on page, clear it and then Enter Username as "Admin" ')
usernameElement = driver.find_element_by_id('txtUsername')
usernameElement.clear()
usernameElement.send_keys('Admin')

print('Step 4 : Find the Password Input Box on a page, clear it and then Enter Username as "admin123" ')
passwordElement = driver.find_element_by_id('txtPassword')
passwordElement.clear()
passwordElement.send_keys('admin123')

print('Step 5 : Find the Submit button on a page, click on it')
loginButton = driver.find_element_by_id('btnLogin')
loginButton.is_selected()
loginButton.is_enabled()
loginButton.click()

