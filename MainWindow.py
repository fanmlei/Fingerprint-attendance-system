# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QTableWidgetItem
from Ui_MainWindow import Ui_MainWindow
from connect_device import ConnetDevice
from database import Database
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    主窗口
    type：QMainWindow
    """
    def __init__(self, id, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        #lo = Login()
        #lo.exec_()
        #获取登录用户名
        self.id = id
        self.name = Database().get_user_info(self.id)['name']
        self.setWindowTitle('指纹考勤系统：%s'%(self.name))
        
        #不是管理员用户是屏蔽部分功能
        if self.name != 'admin':
            self.menu_3.setEnabled(False)
            self.action_9.setEnabled(False)
            self.menu_5.setEnabled(False)
        #隐藏所有tabPage
        for i in range(0, 5):
            self.tabWidget.removeTab(0)
    
    @pyqtSlot()
    def on_action_QT_triggered(self):
        """
        调出QT介绍对话框
        user : all
        """
        QMessageBox.aboutQt(self, u'关于Qt')
        
    @pyqtSlot()
    def on_action_6_triggered(self):
        """
        显示用户信息page
        user ：all
        """
        self.tabWidget.removeTab(0)  #除去原有page
        self.tabWidget.addTab(self.tabWidgetPage1, '用户信息') #添加新的page
        #从数据库中取出用户信息
        info = Database().get_user_info(self.id)
        #更新表单
        self.label_2.setText(info['name']) #name
        self.label_3.setText(info['sex']) #sex
        self.label_4.setText(str(info['finger_id'])) #finger_id
        self.label_11.setText(info['job']) #job
        self.label_12.setText(info['address']) #address
        self.label_13.setText(str(info['tel'])) #tel
        self.label_16.setText(str(info['age'])) #age
        
    @pyqtSlot()
    def on_action_7_triggered(self):
        """
        修改用户信息page
        user : all
        """
        self.tabWidget.removeTab(0)  #除去原有page
        self.tabWidget.addTab(self.tabWidgetPage2, '修改信息') #添加新的page
        #从数据库中取出用户信息
        info = Database().get_user_info(self.id)
        #更新表单
        self.label_18.setText(str(info['id']))
        self.lineEdit.setText(info['name'])
        self.lineEdit_2.setText(info['sex'])
        self.lineEdit_3.setText(info['job'])
        self.lineEdit_4.setText(str(info['age']))
        self.lineEdit_5.setText(info['address'])
        self.lineEdit_6.setText(str(info['tel']))
        
    @pyqtSlot()
    def on_action_3_triggered(self):
        """
        考勤记录
        显示考勤记录页面
        user : all
        """
        self.tabWidget.removeTab(0)  #除去原有page
        self.tabWidget.addTab(self.tabWidgetPage3, '考勤记录') #添加新的page
        self.tableWidget_3.setColumnCount(5)
        self.tableWidget_3.setRowCount(100)
        self.tableWidget_3.setColumnWidth(0,150)
        self.tableWidget_3.setHorizontalHeaderLabels(["时间", "工号", "姓名", "操作记录", "是否违规"])
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.verticalHeader().setStretchLastSection(True)
        record = Database().get_record_by_id(self.id)
        for index,  value in enumerate(record):
            row = 0
            for key in value.keys():
                item = QTableWidgetItem(str(value[key]))
                item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)   #设置表格内容居中
                self.tableWidget_3.setItem(index, row,item)  
                row += 1
    
    @pyqtSlot()
    def on_action_9_triggered(self):
        """
        统计
        显示统计页面
        user ：管理员用户
        """
        Database().new_record(2, 2)  #测试打卡功能
        
        self.tabWidget.removeTab(0)  #除去原有page
        self.tabWidget.addTab(self.tabWidgetPage4, '统计') #添加新的page
        self.tableWidget_4.setColumnCount(5)
        self.tableWidget_4.setRowCount(100)
        self.tableWidget_4.setColumnWidth(0,150)
        self.tableWidget_4.setHorizontalHeaderLabels(["时间", "工号", "姓名", "操作记录", "是否违规"])
        self.tableWidget_4.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_4.verticalHeader().setStretchLastSection(True)
        record = Database().get_record()
        for index,  value in enumerate(record):
            row = 0
            for key in value.keys():
                item = QTableWidgetItem(str(value[key]))
                item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)   #设置表格内容居中
                self.tableWidget_4.setItem(index, row,item)  
                row += 1
        
    @pyqtSlot()
    def on_action_5_triggered(self):
        """
        连接指纹识别器
        user ：管理员用户
        """
        device = ConnetDevice()
        device.exec_()
        
    @pyqtSlot()    
    def on_pushButton_3_clicked(self):
        """
        更新用户数据
        """
        #获取用户重新输入的信息
        id = int(self.label_18.text())
        name = self.lineEdit.text()
        sex = self.lineEdit_2.text()
        job = self.lineEdit_3.text()
        age = int(self.lineEdit_4.text())
        address = self.lineEdit_5.text()
        tel = int(self.lineEdit_6.text())
        info ={'id':id, 'name':name,'age':age,'sex':sex,'address':address,'tel':tel,'job':job}
        Database().change_user_info(info)
        QMessageBox.information(self, 'OK', '用户信息修改成功！')
        
    @pyqtSlot()    
    def on_pushButton_4_clicked(self):
        '''
        放弃按钮
        关闭修改窗口，回到显示信息的窗口
        '''
        self.tabWidget.removeTab(0)  #除去原有page
        self.tabWidget.addTab(self.tabWidgetPage1, '用户信息') #添加新的page
        info = Database().get_user_info(self.id)
        
        #更新表单
        self.label_2.setText(info['name']) #name
        self.label_3.setText(info['sex']) #sex
        self.label_4.setText(str(info['finger_id'])) #finger_id
        self.label_11.setText(info['job']) #job
        self.label_12.setText(info['address']) #address
        self.label_13.setText(str(info['tel'])) #tel
        self.label_16.setText(str(info['age'])) #age
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow(1)
    ui.show()
    sys.exit(app.exec_())
    
    
