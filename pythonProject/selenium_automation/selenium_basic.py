import time
from selenium import webdriver
import json

def get_driver_path(whichbrowser):
    with open('drivers_path.json') as file:
         jsondata = json.load(file)
         if whichbrowser == "CHROME":
            return jsondata.get("CHROME_DRIVER_PATH")
         elif whichbrowser == 'FIREFOX':
            return jsondata.get("FIREFOX_DRIVER_PATH")

driver=None
def launch_browser(whichbrowser="C"):
    global driver
    print("Step1: Launch Browser")
    if whichbrowser =="C":
        driver = webdriver.Chrome(executable_path=get_driver_path('CHROME'))
    elif whichbrowser == "F":
        driver = webdriver.firefox(executable_path=get_driver_path('FIREFOX'))
    elif whichbrowser =="E":
        driver = webdriver.Edge(executable_path=get_driver_path('EDGE'))
    elif whichbrowser =="S":
        driver = webdriver.Safari(executable_path=get_driver_path('SAFARI'))
    print("Step2: Enter URL into Address bar")
    driver.get("https://opensource-demo.orangehrmlive.com/")
    return driver

cnt = 1

def test_orange_hrm_loginpage(cred):
    print('CRED', cred)
    global cnt
    username = "" if cred[0] == 'None' else cred[0]
    password = "" if cred[1] == 'None' else cred[1]

    driver= launch_browser('C')
    usernameInput = driver.find_element_by_id('txtUsername')
    passwordInput = driver.find_element_by_id('txtPassword')
    loginButton = driver.find_element_by_id('btnLogin')

    #time.sleep(2)
    print('Step 3: Enter Username')
    usernameInput.send_keys(username)
    #time.sleep(2)
    print('Step 4: Enter Password')
    passwordInput.send_keys(password)
    #time.sleep(2)
    print('Step 5: Click On login Button')
    loginButton.click()

    errorwebele = None
    try:
       errorwebele = driver.find_element_by_id('spanMessage')
    except:
        pass

    subcribetion = None
    try:
        subcribetion = driver.find_element_by_id('Subscriber_link')
    except:
         pass

    if cred[2] == 'Success':
        assert subcribetion != None
        assert errorwebele == None
    else:
        assert cred[2] == errorwebele.text
        assert subcribetion == None
        assert errorwebele != None


    driver.save_screenshot(f'{cnt}.png')
    time.sleep(3)
    cnt = cnt + 1
    driver.close()


import readexceltestdata

credentials = readexceltestdata.credentials

for cred in credentials:
    test_orange_hrm_loginpage(cred)






import sys
sys.exit(0)

import json
f = open ('drivers_path.json',)
data = json.load(f)
for i in data['drivers_path']:
    print(i)
f.close()



