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
    link_elements = driver.find_element(By.XPATH, "//*[@data-menu-xmlid='om_hospital.menu_appointment_root']")
    if  link_elements :
        link_elements.click()
        time.sleep(2)
    else:
        test_passed = False
        print ('test failed')


if test_passed :
    link_elements = driver.find_element(By.XPATH, "//*[@data-menu-xmlid='om_hospital.menu_appointment']")
    if  link_elements :
        print(link_elements.get_attribute('innerHTML'))
        link_elements.click()
        time.sleep(2)
    else:
        test_passed = False
        print ('test failed')

if test_passed:
     # wait for URL to change with 15 seconds timeout
    WebDriverWait(driver, 5).until(EC.url_changes(currentURL))
    currentURL = driver.current_url
    print(currentURL)

if test_passed:
    time.sleep(2)
    appointment_ref = driver.find_element(By.XPATH, "//*[@name='name']")
    if appointment_ref and appointment_ref.get_attribute('innerHTML') :
        appointment_ref.click() 
    else:
        test_passed = False
        print ('test failed')

if test_passed:
     # wait for URL to change with 15 seconds timeout
    WebDriverWait(driver, 5).until(EC.url_changes(currentURL))
    currentURL = driver.current_url
    print(currentURL)

if test_passed :
    button_elements =driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div[1]/button[1]')
    if button_elements:
        if button_elements.get_attribute('innerHTML').strip() == 'Edit':
            button_elements.click()
            time.sleep(2)
    else:
        test_passed = False
        print ('test failed')

if test_passed:
    time.sleep(2)
    input_fields    =   driver.find_elements(By.XPATH,'//input[@type="text"]')
    if len(input_fields) > 0:
        for input_field in input_fields:
            if input_field.get_property("name") == 'date_appointment':
                input_field.clear()
                input_field.send_keys('05/25/2023')
            if input_field.get_property("name") == 'date_checkup':
                input_field.clear()
                input_field.send_keys('05/25/2023 12:30:00')

if test_passed :
    button_elements =driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/button[1]')
    if button_elements:
        if button_elements.get_attribute('innerHTML').strip() == 'Save':
            button_elements.click()
            time.sleep(2)
    else:
        test_passed = False
        print ('test failed')


if test_passed:
    time.sleep(2)
    appointment_date = driver.find_element(By.NAME, "date_appointment")
    appointment_dateCheckup = driver.find_element(By.NAME, "date_checkup")
    if appointment_date and appointment_dateCheckup:
        if appointment_date.get_attribute('innerHTML') == '05/25/2023' and appointment_dateCheckup.get_attribute('innerHTML') == '05/25/2023 12:30:00':
            print("Final : test successful")
        else:
            print("Final : test failed")
    else:
        print("test failed")

