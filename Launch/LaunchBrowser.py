from selenium import webdriver
from Launch.XmlWriter import XmlWriter
# import time

driver = webdriver.Firefox()
# driver = webdriver.PhantomJS("I:/phantomjs/bin/phantomjs.exe")
driver.maximize_window()
url = driver.command_executor._url        # "http://127.0.0.1:60622/hub"
session_id = driver.session_id            # '4e167f26-dc1d-4f51-a207-f761eaf73c31'
print(url, session_id)
# time.sleep(10)

xmlWriter = XmlWriter.getConfigXmlWriter()
xmlWriter.setElementText(".//remote_url", str(url))
xmlWriter.setElementText(".//session_id", str(session_id))
xmlWriter.save()





