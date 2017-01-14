# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Login(object):
    def test_login(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(30)
        base_url = "http://demov6.k3cloud.kingdee.com"
        driver.get(base_url + "/k3cloud/html5/index.aspx")
        driver.find_element_by_css_selector("span.ui-multiselect-label").click()
        li = driver.find_elements_by_tag_name('li')
        for l in li:
            if l.text == '蓝海机械(正式)':
                l.click()
                break

        time.sleep(5)
        driver.find_element_by_css_selector("#ui-multiselect-btn-language > span.ui-multiselect-label").click()
        driver.find_element_by_xpath("//div[@id='ui-multiselect-menu-language']/ul/li/div/span").click()
        driver.find_element_by_css_selector("#ui-multiselect-btn-verifyType > span.ui-multiselect-label").click()
        driver.find_element_by_xpath("//div[@id='ui-multiselect-menu-verifyType']/ul/li/div/span").click()
        driver.find_element_by_id("user").clear()
        driver.find_element_by_id("user").send_keys("demo")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("888888")
        time.sleep(3)
        driver.find_element_by_css_selector("span.ui-button-text").click()
        time.sleep(30)

# if __name__ == "__main__":
#    unittest.main()
