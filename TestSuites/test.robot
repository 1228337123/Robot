*** Settings ***
Library           Selenium2Library
Library           ../Libs/CalculatorLibrary.py
Library           ../Libs/Login.py
Library           ../Launch/GetDriver.py
Library           OperatingSystem

*** Test Cases ***
LoginCase
    Open Browser    http://demov6.k3cloud.kingdee.com/k3cloud/html5/index.aspx
    Sleep    10
    Input Text    id = user    demo
    Input Text    id = password    888888
    Click Element    id=ui-multiselect-btn-datacenter
    Click Element    id = ui-multiselect-datacenter-option-0
    Click Button    css = .ui-button-text
    Sleep    5

test_get_driver
    ${driver}    Get Driver
    Log    ${driver}

t_get_browser
    Get Browser    http://baidu.com
    test login
