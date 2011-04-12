from PySide.QtCore import *
from PySide.QtGui import *
import urllib, urllib2


class Websupport:
    def __init__(self):
        self.searchBox = QLineEdit
        self.mangaList = []
        self.syncTitles()
        

    def syncTitles(self): #virtual
        pass

    def listTitles(self):
        for x in self.mangaList:
            print x #placeholder

    def searchTitle(self,name):
        for x in zip(range(len(self.mangaList)),self.mangaList):
            if x[1].find(name) == 0:
                print x[0], x[1]
        
    def browseTitle(self,name):
        self.parseChapters(name)
        #show all available chapters
        #need gui to select chapter?
        #else just start latest or something

    def selectChapter(self,number):
        files = []
        self.createFileList(files)
        self.createSubfolder()
        self.downloadFiles(files)

    def downloadFiles(files):
        print "notImplemented"

    def parseChapters(self,name):
        #fill up self.chapterList
        pass



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


