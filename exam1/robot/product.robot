*** Settings ***
Documentation     Testing product category
Library           SeleniumLibrary

*** Variables ***
${URL}      http://localhost:8015/web/login
${BROWSER}        Chrome



*** Test Cases ***
Valid Product Category

    Set Global Variable    ${URL} 
    Open Browser To Login Page                            # step 1
    Input Username    subhadipsjsc@gmail.com              # step 2
    Input Password    admin123                            # step 3
    Submit Credentials                                    # step 4
    handle url change                                     # step 5
    handle url change                                     # step 6
    click on home menu                                    # step 7
    click on lunch menu                                   # step 8
    handle url change                                     # step 9
    click on Configuration                                # step 10
    click on Product Category                             # step 11
    handle url change                                     # step 12
    click on create product category                      # step 13
    handle url change                                     # step 14
    Input product category name     new Product category  # step 15 
    click on save product category                        # step 16
    handle url change                                     # step 17
    click on Configuration                                # step 18                      
    click on Product Category                             # step 19 
    click on account logo                                 # step 20
    click on logout                                       # step 21
    Sleep    10s                                          # step 22


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
    Should Be True     """${inner html}""".strip() == "Log out fail"
    Click Link     xpath://a[@href="http://localhost:8015/web/session/logout"]

click on home menu
    Sleep    3s
    Click Button    xpath:/html/body/header/nav/div[1]/button

click on lunch menu
    Sleep    3s
    ${inner html} =    Get Element Attribute    xpath:/html/body/header/nav/div[1]/div/a[8]    innerHTML
    Should Be True     """${inner html}""".strip() == "Lunch"
    Click Link  xpath:/html/body/header/nav/div[1]/div/a[8]

click on Configuration
    Sleep    3s
    ${inner html} =    Get Element Attribute    xpath://*[@data-menu-xmlid='lunch.menu_lunch_config']    innerHTML
    Click Button  xpath://*[@data-menu-xmlid='lunch.menu_lunch_config']

click on Product Category
    Sleep    3s
    ${inner html} =    Get Element Attribute    xpath://*[@data-menu-xmlid="lunch.lunch_product_category_menu"]    innerHTML
    Should Be True     """${inner html}""".strip() == "Product Categories"
    Click Link   xpath://*[@data-menu-xmlid="lunch.lunch_product_category_menu"]

click on create product category
    Sleep    3s
    ${inner html} =    Get Element Attribute    xpath:/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/button[3]    innerHTML
    Should Be True     """${inner html}""".strip() == "Create"
    Click Button   xpath:/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/button[3]

Input product category name
    [Arguments]    ${product category name}
    Input Text    name:name    ${product category name}

click on save product category
    Sleep    3s
    ${inner html} =    Get Element Attribute     xpath:/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/button[1]   innerHTML
    Should Be True     """${inner html}""".strip() == "Save"
    Click Button   xpath:/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/button[1]

    