from selenium import webdriver

CHROME_DRIVER_PATH = 'D:\\pythonProject\\selenium_automation\\drivers\\chromedriver.exe'

driver = webdriver.Chrome(executable_path = CHROME_DRIVER_PATH)

APPLICATION_URL = 'https://opensource-demo.orangehrmlive.com/'
webelement = driver.find_element_by_id('btnLogin')
webelement.is_displayed()
webelement.is_selected()
