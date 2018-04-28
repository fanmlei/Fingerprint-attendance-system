# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from Ui_connect_device import Ui_Dialog
from device import Device
#from PyQt5.QtSerialPort import QSerialPortInfo, QSerialPort
import serial, serial.tools.list_ports, threading
import sys

class ConnetDevice(QDialog, Ui_Dialog):
    """
    type:QDialog
    连接指纹识别器
    """
    def __init__(self, parent=None):
        super(ConnetDevice, self).__init__(parent)
        self.setupUi(self)
        #设置下拉框不可选中
        self.groupBox.setEnabled(False)
        self.groupBox_2.setEnabled(False)
        
    @pyqtSlot()
    def on_buttonBox_accepted(self):
        """
        OK按钮事件
        """
        #判断串口button是否被选中
        if self.radioButton.isChecked():
            self.port_name = self.comboBox.currentText()
            self.baud_rate = int(self.comboBox_3.currentText())
            
            self.device = Device(self.port_name, self.baud_rate)
            t = threading.Thread(target=self.device.recive_data)
            t.start()
            
            #if device.port.isOpen():
                #QMessageBox.information(None, '提示', '设备连接成功！    ')

    @pyqtSlot()
    def on_buttonBox_rejected(self):
        """
        cancel事件
        """
        self.reject()
        
    @pyqtSlot()
    def on_radioButton_clicked(self):
        """
        串口按钮
        激活选择区域并更新选项
        """
        self.groupBox.setEnabled(True)
        self.serial_comboBox_init()
        
    @pyqtSlot()
    def on_radioButton_2_clicked(self):
        """
        蓝牙按钮
        由于适配问题暂时屏蔽掉
        """
        QMessageBox.information(self,'提示','由于环境适配问题暂时不开放，请留意后续更新')
        
    def serial_comboBox_init(self):
        '''
        初始化串口连接下拉框     
        '''
        baud_rate = ['9600','19200','38400','43000','56000','57600','115200']
        self.comboBox_3.addItems(baud_rate)
        plist = list(serial.tools.list_ports.comports())
        if len(plist) > 0:
            for i in plist:
                self.comboBox.addItem(i[0])
            
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = ConnetDevice()
    ui.show()
    sys.exit(app.exec_())
    
    
    
