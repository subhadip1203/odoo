import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option("detach",True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()) , options=options )

test_passed = True
driver.get("http://localhost:8015/")
driver.maximize_window()

currentURL = ""

time.sleep(1)
link = driver.find_element('xpath' , '//*[@id="top_menu"]/li[9]/a')
if link and link.get_attribute('innerHTML') == 'Sign in':
    link.click()
else:
    test_passed = False
    print ('test failed')

if test_passed :
    time.sleep(1)
    login_element   =   driver.find_element(By.ID,'login')
    pass_element    =   driver.find_element(By.ID,'password')
    button_element  =   driver.find_element(By.XPATH, '//*[@id="wrapwrap"]/main/div/form/div[3]/button')
    if login_element and pass_element and button_element :
        login_element.send_keys('subhadipsjsc@gmail.com')
        pass_element.send_keys('admin123')
        time.sleep(1)
        button_element.click()
    else:
        test_passed = False
        print ('test failed')

if test_passed:
     # wait for URL to change with 15 seconds timeout
    WebDriverWait(driver, 10).until(EC.url_changes('http://localhost:8015/web/login'))
    currentURL = driver.current_url

    # wait for URL to change with 15 seconds timeout
    WebDriverWait(driver, 5).until(EC.url_changes(currentURL))
    currentURL = driver.current_url
    print(currentURL)

    dashboard_element  =   driver.find_element(By.XPATH, '/html/body/header/nav/div[1]/button')
    if dashboard_element.get_attribute('innerHTML')  == '<i class="fa fa-th-large"></i>':
        time.sleep(2)
        dashboard_element.click()
        time.sleep(2)
    else:
        test_passed = False
        print ('test failed')

if test_passed :
    link_elements =driver.find_element(By.XPATH, "//*[@data-menu-xmlid='om_hospital.menu_hospital_root']")
    if link_elements and link_elements.get_attribute('innerHTML') == 'Hospital':
        link_elements.click()
    else:
        test_passed = False
        print ('test failed')

if test_passed:
     # wait for URL to change with 15 seconds timeout
    WebDriverWait(driver, 5).until(EC.url_changes(currentURL))
    currentURL = driver.current_url
    print(currentURL)

if test_passed :
    button_elements =driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/button[3]')
    if button_elements and button_elements.get_attribute('innerHTML').strip() == 'Create':
        button_elements.click()
        time.sleep(2)
    else:
        test_passed = False
        print ('test failed')

if test_passed:
     # wait for URL to change with 15 seconds timeout
    WebDriverWait(driver, 5).until(EC.url_changes(currentURL))
    currentURL = driver.current_url
    print(currentURL)


randomNumber = random.randrange(1,9999999)
globalName = 'test patient '+str(randomNumber)
globalAge = '25'
globalGender = 'Female'
globalDescription = 'new patient '+ str(randomNumber)

if test_passed :
    time.sleep(2)
    name            =   driver.find_element(By.NAME,'name')
    age             =   driver.find_element(By.NAME,'age')
    gender          =   driver.find_element(By.NAME,'gender')
    description     =   driver.find_element(By.NAME,'note')
    saveButton      =   driver.find_element(By.XPATH, "//*[@title='Save record']") 
    if name  and age and gender and  description and saveButton:
       
        name.clear()
        name.send_keys(globalName)
        age.clear()
        age.send_keys(globalAge)
        gender.send_keys(globalGender)
        description.clear()
        description.send_keys(globalDescription)
        time.sleep(2)
        saveButton.click()
    else:
        test_passed = False
        print('test Failed')

if test_passed:
     # wait for URL to change with 15 seconds timeout
    WebDriverWait(driver, 5).until(EC.url_changes(currentURL))
    currentURL = driver.current_url
    print(currentURL)
    




if test_passed :
    time.sleep(2)
    link_elements =driver.find_element(By.XPATH, '/html/body/header/nav/div[2]/div[1]/button')
    if link_elements and link_elements.get_attribute('innerHTML') == '<span data-section="269">Patients</span>':
        link_elements.click()
        
    else:
        test_passed = False
        print ('test failed')

if test_passed:
    time.sleep(5)
    link_elements = driver.find_element(By.XPATH, "//*[@data-menu-xmlid='om_hospital.menu_patient']")
    if  link_elements and link_elements.get_attribute('innerHTML') == 'Patients' :
        link_elements.click()
        
    else:
        test_passed = False
        print ('test failed')

if test_passed:
    time.sleep(2)
    cols = driver.find_elements(By.CSS_SELECTOR, "td:nth-child(3)")
    for col in cols:
        # print(col.get_attribute('innerHTML'),globalName , col.get_attribute('innerHTML') == globalName)
        if col.get_attribute('innerHTML') == globalName:
            col.click()

if test_passed:
     # wait for URL to change with 15 seconds timeout
    WebDriverWait(driver, 5).until(EC.url_changes(currentURL))
    currentURL = driver.current_url
    print(currentURL)


if test_passed :
    time.sleep(5)
    name            =   driver.find_element(By.XPATH, "//*[@name='name']")
    age             =   driver.find_element(By.XPATH, "//*[@name='age']")
    gender          =   driver.find_element(By.XPATH, "//*[@name='gender']")
    description     =   driver.find_element(By.XPATH, "//*[@name='note']")
    if name  and age and gender and  description :
        # print(name.get_attribute('innerHTML'), globalName) 
        # print(age.get_attribute('innerHTML'), globalAge)  
        # print(gender.get_attribute('innerHTML'), globalGender)   
        # print(description.get_attribute('innerHTML'), globalDescription)  
        
        if name.get_attribute('innerHTML')!= globalName :
           print ('Final : test Failed , name not matched')
        elif  age.get_attribute('innerHTML') != globalAge :
            print ('Final : test Failed , age not matched')
        elif gender.get_attribute('innerHTML') != globalGender :
            print ('Final : test Failed , gender not matched')
        elif description.get_attribute('innerHTML') != globalDescription :
            print ('Final : test Failed , description not matched')
        else:
            print ('Final : test Passed') 
    else:
        print ('test Failed')    

        