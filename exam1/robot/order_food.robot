*** Settings ***
Documentation     Testing user ordering food 
Library           SeleniumLibrary

*** Variables ***
${URL}      http://localhost:8015/web/login
${BROWSER}        Chrome



*** Test Cases ***
Valid order food
    Set Global Variable    ${URL} 
    Open Browser To Login Page                        # step 1
    Input Username    subhadipsjsc@gmail.com          # step 2
    Input Password    admin123                        # step 3
    Submit Credentials                                # step 4
    handle url change                                 # step 5
    handle url change                                 # step 6
    click on home menu                                # step 7
    click on lunch menu                               # step 8
    handle url change                                 # step 9
    click on first food item                          # step 10
    Input Note for order  please add extra Cheese     # step 11
    click add to cart                                 # step 12
    click order now                                   # step 13
    delete an order                                   # step 14
    click on account logo                             # step 15
    click on logout                                   # step 16
    Sleep    10s                                      # step 17


*** Keywords ***

Open Browser To Login Page
    Open Browser    ${URL}    ${BROWSER}
    Title Should Be    Login | My Website

Input Username
    [Arguments]    ${username}
    Input Text    name:login    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    name:password    ${password}

Submit Credentials
    Click Button    xpath://*[@id="wrapwrap"]/main/div/form/div[3]/button[1]

handle url change
    ${URL}  Get Location
    Log To Console  ${URL}
    Sleep    1s

click on account logo
    Sleep    3s
    ${inner html} =    Get Element Attribute   class:oe_topbar_name    innerHTML
    Should Be True     """${inner html}""".strip() == "Administrator"
    Click Element    class:oe_topbar_name

click on logout
    Sleep    3s
    ${inner html} =    Get Element Attribute   xpath://a[@href="http://localhost:8015/web/session/logout"]    innerHTML
    Should Be True     """${inner html}""".strip() == "Log out"
    Click Link     xpath://a[@href="http://localhost:8015/web/session/logout"]

click on home menu
    Sleep    3s
    Click Button    xpath:/html/body/header/nav/div[1]/button

click on lunch menu
    Sleep    3s
    ${inner html} =    Get Element Attribute    xpath:/html/body/header/nav/div[1]/div/a[8]    innerHTML
    Should Be True     """${inner html}""".strip() == "Lunch"
    Click Link  xpath:/html/body/header/nav/div[1]/div/a[8]

click on first food item
    Sleep    3s
    Click Element      class:o_kanban_record

Input Note for order
    Sleep    4s
    [Arguments]    ${note}
    Input Text    name:note    ${note}

click add to cart
    Sleep    4s
    Click Button    name:add_to_cart

click order now
    Sleep    4s
    Click Button     xpath:/html/body/div[1]/div/div[2]/div[2]/span/div/div/div[3]/div/button

delete an order
    Sleep    4s
    Click Button     xpath:/html/body/div[1]/div/div[2]/div[2]/span/div/div/div[2]/div/h4/button

