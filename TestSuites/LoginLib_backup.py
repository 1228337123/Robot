# coding: utf-8

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time


class LoginLib(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://demov6.k3cloud.kingdee.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url + "/k3cloud/html5/index.aspx")
        driver.find_element_by_css_selector("span.ui-multiselect-label").click()
        li = driver.find_elements_by_tag_name('li')
        for l in li:
            if l.text == u'蓝海机械(正式)':
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

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
