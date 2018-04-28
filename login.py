# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.QtGui import QCursor, QMovie
from PyQt5.QtCore import pyqtSlot, Qt
from Ui_login import Ui_Dialog
from database import Database
from finger_input import FingerInput
#from connect_device import ConnetDevice
from device import Device
import sys, time


class Login(QDialog, Ui_Dialog):
    """
    用户登录接口
    type：QDialog
    """
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        self.gif = QMovie('qqloading.gif')
        self.label.setMovie(self.gif)
        self.gif.start()
        self.setWindowFlags(Qt.FramelessWindowHint)
        
    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  #更改鼠标图标
            
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:  
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
            QMouseEvent.accept()
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QCursor(Qt.ArrowCursor))
        
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        关闭窗口
        """
        self.close()
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        最小化窗口
        """
        self.showMinimized()
        
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        """
        验证用户
        """
        user_id= int(self.lineEdit.text())
        passwd = self.lineEdit_2.text()
        if  passwd == Database().get_passwd(user_id):
            self.accept()
            self.id = user_id
        else:
            QMessageBox.warning(self,'错误','请检查用户名密码后重新输入')
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            
    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        """
        用户名清空
        """
        self.lineEdit.clear()
    
    @pyqtSlot()
    def on_pushButton_5_clicked(self):
        """
        密码清空
        """
        self.lineEdit_2.clear()
    
    @pyqtSlot()
    def on_pushButton_6_clicked(self):
        """
        用户注册
        """
        pass
    
    @pyqtSlot()
    def on_pushButton_7_clicked(self):
        """
        指纹验证登录
        """
        f_input = FingerInput()
        f_input.accept()
        #f_input.exec_()
        d = Device("COM9",9600)
        
        self.accept()
        self.id = int(d.get_finger_id())
        #self.id = f_input.id

        #f_input.closeSignal.emit()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Ui = Login()
    Ui.show()
    sys.exit(app.exec_())
