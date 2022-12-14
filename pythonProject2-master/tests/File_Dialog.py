# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 13:56:04 2022

@author: marvin
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog

class fileDialog(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.openFileNameDialog()
    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = fileDialog()
    sys.exit(app.exec_())