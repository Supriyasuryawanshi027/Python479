from selenium import webdriver

CHROME_DRIVER_PATH = 'D:\\pythonProject\\selenium_automation\\drivers\\chromedriver.exe'
APP_PATH = 'file:///C:/Users/shivkumar/Desktop/Windows/a.html'

print('Step 1: Launch the browser')
driver = webdriver.Chrome(executable_path = CHROME_DRIVER_PATH)
driver.get(APP_PATH)