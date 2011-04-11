import sys, os
from PySide.QtCore import *
from PySide.QtGui import *


imagetypes = ('.jpg', '.jpeg', '.png')


class Reader:
    def __init__(self):
        self.label = QLabel()
        self.label.show()
        self.imageList = []
        self.imageListCounter = 0
        self.changeDirectory(os.getcwd())

    def listDirectory(self):
        print self.currentDirectory
        for f in os.listdir(self.currentDirectory):
            if os.path.splitext(f)[1].lower() in imagetypes:
                self.imageList.append(os.path.join(self.currentDirectory, f))

    def showNextImage(self):
        if len(self.imageList) != 0:
            self.label.setPixmap(QPixmap(self.imageList[self.imageListCounter]))
            self.label.adjustSize()
            self.imageListCounter = (self.imageListCounter + 1) % len(self.imageList)

    def changeDirectory(self, directory):
        self.imageList = []
        self.currentDirectory = directory
        self.listDirectory()
        self.showNextImage()
