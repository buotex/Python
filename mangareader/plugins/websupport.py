from PySide.QtCore import *
from PySide.QtGui import *
import urllib, urllib2, re
import os


class Websupport:
    def __init__(self):
        self.mangaList = []
        #self.syncTitles()
        
    def lookFor(self, name):
        pass

    def selectChapter(self,number):
        files = []
        self.createFileList(files)
        self.createSubfolder()
        self.downloadFiles(files)

    def downloadFiles(self, imgLinks, target):
        os.mkdir(target)
        for link in imgLinks:
            response = urllib2.urlopen(link)
            filename = re.search('[^/]*$',link).group(0)
            file = open(target + filename,"w")
            file.write(response.read())
            file.close()

#Searchbox:
class SearchBox:
    def __init__(self):
        self.input = QLineEdit()
        self.popup = QComboBox()
        self.popup.setGeometry(0,self.input.height(), 0,0)

    def search(self, name, nameList):
        for x in nameList:
            if nameList.find(name) == 0:
                self.popup.addItem(QString(x))





