import time
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

if test_passed :
    # wait for URL to change with 15 seconds timeout
    WebDriverWait(driver, 10).until(EC.url_changes('http://localhost:8015/web/login'))
    new_url = driver.current_url

    # wait for URL to change with 15 seconds timeout
    WebDriverWait(driver, 5).until(EC.url_changes(new_url))
    new_url = driver.current_url
    print(new_url)

    user_topbar_name = driver.find_element(By.CLASS_NAME, 'oe_topbar_name')
    if user_topbar_name and user_topbar_name.get_attribute('innerHTML') == 'Administrator' :
        user_topbar_name.click()
    else:
        test_passed = False
        print ('test failed')

if test_passed :
    my_profile =driver.find_element(By.XPATH, '/html/body/header/nav/div[2]/div[4]/div/span[2]')
    if(my_profile.get_attribute('innerHTML') == 'My Profile'):
        time.sleep(2)
        my_profile.click()
    else:
        test_passed = False
        print ('test failed')

if test_passed :
    WebDriverWait(driver, 5).until(EC.url_changes(new_url))
    element1=driver.find_element(By.ID,'o_field_input_11')
    element2=driver.find_element(By.ID,'o_field_input_18')
    if(element1.get_attribute('innerHTML') == element2.get_attribute('innerHTML') == 'subhadipsjsc@gmail.com') :
        print('test passed')
    else:
        test_passed = False
        print('test Failed')

if test_passed :
    user_topbar_name = driver.find_element(By.CLASS_NAME, 'oe_topbar_name')
    if user_topbar_name and user_topbar_name.get_attribute('innerHTML') == 'Administrator' :
        user_topbar_name.click()
    else:
        test_passed = False
        print ('test failed')

if test_passed :
    logout_element =driver.find_element(By.XPATH, '//a[@href="http://localhost:8015/web/session/logout"]')
    if logout_element and logout_element.get_attribute('innerHTML') == 'Log out':
        time.sleep(2)
        logout_element.click()
    else:
        test_passed = False
        print ('test failed')


if test_passed :
    WebDriverWait(driver, 5).until(EC.url_changes(new_url))
    new_url = driver.current_url
    if new_url == 'http://localhost:8015/web/login':
        print ('test Passed')
    else:
        print ('test failed')

