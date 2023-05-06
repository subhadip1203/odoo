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
    link_elements =driver.find_element(By.XPATH, "//*[@data-menu-xmlid='fleet.menu_root']")
    if link_elements and link_elements.get_attribute('innerHTML') == 'Fleet':
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
    link_elements = driver.find_element(By.XPATH, "//*[@data-menu-xmlid='fleet.fleet_configuration']")
    if  link_elements :
        link_elements.click()
        time.sleep(2)
    else:
        test_passed = False
        print ('test failed')


if test_passed :
    link_elements = driver.find_element(By.XPATH, "//*[@data-menu-xmlid='fleet.fleet_config_settings_menu']")
    if  link_elements :
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

if test_passed :
    time.sleep(2)
    div_elements = driver.find_elements(By.CLASS_NAME, "app_name")
    if len(div_elements) > 0:
        for div in div_elements :
            textVal =  div.get_attribute('innerHTML')
            if textVal.strip() == 'General Settings':
                div.click()
                break
    else:
        print ('div not found : test failed')

 

if test_passed :
    button_elements =driver.find_element(By.XPATH, '//*[@id="active_user_setting"]/div/button')
    if button_elements:
        textVal =  button_elements.find_element(By.XPATH,".//span[text()]").text
        if textVal == 'Manage Users':
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

if test_passed :
    button_elements =driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/button[3]')
    if button_elements:
        if button_elements.get_attribute('innerHTML').strip() == 'Create':
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
g_name = 'user '+str(randomNumber)
g_email = 'user'+str(randomNumber)+'@email.com'
if test_passed :
    name =   driver.find_element(By.NAME,'name')
    email   =   driver.find_element(By.NAME,'login')
    button_elements   =   driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/button[1]')
    if name and email  and button_elements :
        time.sleep(1)
        name.clear()
        name.send_keys(g_name)
        time.sleep(1)
        email.clear()
        email.send_keys(g_email)
        time.sleep(2)
        button_elements.click()
    else:
        test_passed = False
        print('test Failed')

if test_passed:
     # wait for URL to change with 15 seconds timeout
    WebDriverWait(driver, 5).until(EC.url_changes(currentURL))
    currentURL = driver.current_url
    print(currentURL)
    print("test done")

   