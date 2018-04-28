# -*- coding: utf-8 -*-

"""
Module implementing FingerInput.
"""

from PyQt5.QtCore import pyqtSlot, Qt,  pyqtSignal
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QDialog , QApplication
from device import Device
from Ui_finger_input import Ui_Dialog
import sys

class FingerInput(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    #自定义关闭信号
    closeSignal = pyqtSignal()
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        
        super(FingerInput, self).__init__(parent)
        self.setupUi(self)
        self.gif = QMovie('finger_input.gif')
        self.label.setMovie(self.gif)
        self.gif.start()
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        d = Device("COM9", 9600)
        self.id = int(d.get_finger_id())
        
        self.closeSignal.connect(self.close)
        
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        self.close()
    
      
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Ui = FingerInput()
    Ui.show()
    sys.exit(app.exec_())
    
    
