import sys, os
from PySide.QtCore import *
from PySide.QtGui import *

import plugins.websupport import Websupport

imagetypes = ('.jpg', '.jpeg', '.png')


#Show window



app = QApplication(sys.argv)


reader = Reader()


button = QPushButton('Click me')
button.clicked.connect(reader.showNextImage)
button.show()

app.exec_()
sys.exit()








#
