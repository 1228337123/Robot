# coding=UTF-8
from xml.etree.ElementTree import ElementTree
import os

# configPath = "R:\\K3CloudTest\\DataPool\\config.xml"
# configPath = 'E:\Robot\Launch\config.xml'


class XmlWriter(object):
    def __init__(self, file):
        self.file = file
        self.tree = ElementTree(file=file)

    def __del__(self):
        del self.tree

    def setElementText(self, path, text):
        elem = self.tree.find(path)
        elem.text = text

    def setElementAttr(self, path, attr, value):
        self.tree.find(path).set(attr, value)

    def save(self):
        self.tree.write(self.file, "UTF-8")

    configXmlWriter = None

    # @staticmethod
    def getConfigXmlWriter(self,xmlpath):
        if XmlWriter.configXmlWriter is None:
            # path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../config.xml'))
            # XmlWriter.configXmlWriter = XmlWriter(path)
            XmlWriter.configXmlWriter = XmlWriter(xmlpath)
        return XmlWriter.configXmlWriter
