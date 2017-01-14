# coding=UTF-8
from selenium import webdriver
# import time
from Launch.XmlReader import XmlReader


class GetDriver(object):

    def get_driver(self):
        xml = XmlReader.getConfigXmlReader()
        remote_url = xml.getElementText(".//remote_url")
        session_id = xml.getElementText(".//session_id")
        driver = webdriver.Remote(command_executor=remote_url, desired_capabilities={})
        driver.session_id = session_id
        return driver
        # driver.get("http://www.youdao.com")

    def get_browser(self, url):
        driver = GetDriver.get_driver(self)
        driver.get(url)
