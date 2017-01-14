# coding=UTF-8
from xml.etree.ElementTree import ElementTree
import os

# configPath = "R:\\K3CloudTest\\DataPool\\config.xml"
# configPath = 'E:\Robot\Launch\config.xml'
class XmlReader(object):
    configXmlReader = None

    def __init__(self, file):
        self.tree = ElementTree(file=file)

    def getElementAttr(self, xpath, attr):
        return self.tree.find(xpath).get(attr)

    def getElementText(self, xpath):
        return self.tree.find(xpath).text

    # @staticmethod
    def getConfigXmlReader(self, xmlpath):
        if XmlReader.configXmlReader is None:
            # path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../config.xml'))
            # XmlReader.configXmlReader = XmlReader(path)
            XmlReader.configXmlReader = XmlReader(xmlpath)
        return XmlReader.configXmlReader
