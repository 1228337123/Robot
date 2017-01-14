from selenium import webdriver
# import time
from Utils.XmlReader import XmlReader
from Utils.XmlWriter import XmlWriter

xmlpath = "E:\Robot\UI\Login.xml"
xml = XmlReader(xmlpath).getConfigXmlReader(xmlpath)
url = xml.getElementText(".//base_url")
id = xml.getElementText(".//add_url")

print (url,id)

xmlWriter = XmlWriter(xmlpath).getConfigXmlWriter(xmlpath)
xmlWriter.setElementText(".//key","haha")
xmlWriter.save()