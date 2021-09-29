from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


CHROME_DRIVER_PATH = 'D:\\pythonProject\\selenium_automation\\drivers\\chromedriver.exe'
APPLICATION_URL = 'https://demoqa.com/automation-practice-form'

print('Step1 : Launch the browser ')
driver = webdriver.Chrome(executable_path = CHROME_DRIVER_PATH)
print('Step2 : Enter Url into Address Bar')
driver.get(APPLICATION_URL)

print('Enter FirstName : ')
driver.find_element_by_id('firstName').send_keys('Supriya')

print('Enter LastName : ')
driver.find_element_by_id('lastName').send_keys('Suryawanshi')

print('Enter Email : ')
driver.find_element_by_id('userEmail').send_keys('Supriya@gmail.com')

print('Select Gender : ')
genders = driver.find_elements_by_xpath('//input[@name="gender"]')
print('element -->', len(genders))  #3
for gen in genders:
    print('gen value',gen.get_attribute('value'))
    if gen.get_attribute('value') == 'Female':
        ActionChains(driver).move_to_element(gen).click(gen).perform()  # mouse or keyboard --> click
        break

'''genderElements = driver.find_elements_by_id('gender')
for gen in genderElements:
    if gen.get_attribute('value')=='Male':
        gen.click()
        break'''

print('Enter Mobile : ')
driver.find_element_by_id('userNumber').send_keys('1234569870')

print('Select DOB : ')
print('Enter Enter Subjects : ')
print('Select Hobbies : ')
sports = driver.find_elements_by_xpath('//input[@type="checkbox"]')
for sp in sports:
    if sp.get_attribute('value') in ['1','3']:
        ActionChains(driver).move_to_element(sp).click(sp).perform()

'''sports = driver.find_elements_by_class_name('custom-control-input')
for sp in sports:
    if sp.get_attribute('value') in ['1','3']:
        sp.click()'''

print('Upload Photo : ')
print('Enter Current Address : ')
print('Select State/City : ')