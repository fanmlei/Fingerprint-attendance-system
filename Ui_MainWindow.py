# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\fml\Desktop\指纹考勤系统\Eric\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 406)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/finger.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, -1, 600, 401))
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidgetPage1 = QtWidgets.QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tabWidgetPage1)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 80, 271, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 6, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 5, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 1, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_16.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tabWidgetPage1)
        self.label_10.setGeometry(QtCore.QRect(190, 10, 101, 21))
        self.label_10.setStyleSheet("font: 87 14pt \"Arial Black\";")
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QtWidgets.QWidget()
        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tabWidgetPage2)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(40, 40, 241, 181))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 3, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_24.setObjectName("label_24")
        self.gridLayout_3.addWidget(self.label_24, 6, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_3.addWidget(self.lineEdit_3, 4, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_27.setObjectName("label_27")
        self.gridLayout_3.addWidget(self.label_27, 5, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 3, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_3.addWidget(self.lineEdit_6, 6, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_28.setObjectName("label_28")
        self.gridLayout_3.addWidget(self.label_28, 1, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_26.setObjectName("label_26")
        self.gridLayout_3.addWidget(self.label_26, 4, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_3.addWidget(self.lineEdit_5, 5, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 2, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_3.addWidget(self.lineEdit_4, 2, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 0, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_18.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 0, 1, 1, 1)
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.tabWidgetPage2)
        self.graphicsView_3.setGeometry(QtCore.QRect(380, 20, 151, 171))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.pushButton = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.pushButton.setGeometry(QtCore.QRect(380, 210, 71, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 210, 71, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 270, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 270, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.pushButton_5.setGeometry(QtCore.QRect(200, 270, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.tabWidgetPage3 = QtWidgets.QWidget()
        self.tabWidgetPage3.setObjectName("tabWidgetPage3")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tabWidgetPage3)
        self.tableWidget_3.setGeometry(QtCore.QRect(-1, -1, 602, 364))
        self.tableWidget_3.setInputMethodHints(QtCore.Qt.ImhDate|QtCore.Qt.ImhTime)
        self.tableWidget_3.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_3.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.verticalHeader().setStretchLastSection(True)
        self.tableWidget_3.raise_()
        self.tableWidget_3.raise_()
        self.tabWidget.addTab(self.tabWidgetPage3, "")
        self.tabWidgetPage4 = QtWidgets.QWidget()
        self.tabWidgetPage4.setObjectName("tabWidgetPage4")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tabWidgetPage4)
        self.tableWidget_4.setGeometry(QtCore.QRect(-1, -1, 602, 364))
        self.tableWidget_4.setInputMethodHints(QtCore.Qt.ImhDate|QtCore.Qt.ImhTime)
        self.tableWidget_4.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_4.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setRowCount(0)
        self.tableWidget_4.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_4.verticalHeader().setStretchLastSection(True)
        self.tabWidget.addTab(self.tabWidgetPage4, "")
        self.tabWidgetPage5 = QtWidgets.QWidget()
        self.tabWidgetPage5.setObjectName("tabWidgetPage5")
        self.tabWidget.addTab(self.tabWidgetPage5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setSeparatorsCollapsible(False)
        self.menu_3.setToolTipsVisible(False)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setCheckable(False)
        self.action_6.setChecked(False)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_8 = QtWidgets.QAction(MainWindow)
        self.action_8.setObjectName("action_8")
        self.action_9 = QtWidgets.QAction(MainWindow)
        self.action_9.setObjectName("action_9")
        self.action_QT = QtWidgets.QAction(MainWindow)
        self.action_QT.setObjectName("action_QT")
        self.action_12 = QtWidgets.QAction(MainWindow)
        self.action_12.setObjectName("action_12")
        self.menu.addAction(self.action_6)
        self.menu.addAction(self.action_7)
        self.menu_2.addAction(self.action_3)
        self.menu_2.addAction(self.action_9)
        self.menu_3.addAction(self.action_8)
        self.menu_4.addAction(self.action_QT)
        self.menu_4.addAction(self.action_12)
        self.menu_5.addAction(self.action_5)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "指纹考勤系统"))
        self.label_9.setText(_translate("MainWindow", "指纹ID："))
        self.label_8.setText(_translate("MainWindow", "职位："))
        self.label_6.setText(_translate("MainWindow", "家庭住址："))
        self.label_7.setText(_translate("MainWindow", "联系电话："))
        self.label.setText(_translate("MainWindow", "姓名："))
        self.label_5.setText(_translate("MainWindow", "性别："))
        self.label_15.setText(_translate("MainWindow", "年龄："))
        self.label_10.setText(_translate("MainWindow", "个人信息"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), _translate("MainWindow", "用户信息"))
        self.label_24.setText(_translate("MainWindow", "联系电话："))
        self.label_27.setText(_translate("MainWindow", "家庭住址："))
        self.label_23.setText(_translate("MainWindow", "性别："))
        self.label_28.setText(_translate("MainWindow", "姓名："))
        self.label_26.setText(_translate("MainWindow", "职位："))
        self.label_14.setText(_translate("MainWindow", "年龄："))
        self.label_17.setText(_translate("MainWindow", "ID："))
        self.pushButton.setText(_translate("MainWindow", "选择文件"))
        self.pushButton_2.setText(_translate("MainWindow", "上传图片"))
        self.pushButton_3.setText(_translate("MainWindow", "保存"))
        self.pushButton_4.setText(_translate("MainWindow", "放弃"))
        self.pushButton_5.setText(_translate("MainWindow", "录入指纹"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), _translate("MainWindow", "修改信息"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage3), _translate("MainWindow", "历史记录"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage4), _translate("MainWindow", "统计"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage5), _translate("MainWindow", "管理"))
        self.menu.setTitle(_translate("MainWindow", "用户管理"))
        self.menu_2.setTitle(_translate("MainWindow", "考勤记录"))
        self.menu_3.setTitle(_translate("MainWindow", "管理"))
        self.menu_4.setTitle(_translate("MainWindow", "帮助"))
        self.menu_5.setTitle(_translate("MainWindow", "连接设置"))
        self.action.setText(_translate("MainWindow", "查看个人信息"))
        self.action_2.setText(_translate("MainWindow", "修改个人信息"))
        self.action_3.setText(_translate("MainWindow", "历史记录"))
        self.action_4.setText(_translate("MainWindow", "连接数据库"))
        self.action_5.setText(_translate("MainWindow", "连接指纹识别器"))
        self.action_6.setText(_translate("MainWindow", "查看个人信息"))
        self.action_7.setText(_translate("MainWindow", "修改个人信息"))
        self.action_8.setText(_translate("MainWindow", "管理指纹信息"))
        self.action_9.setText(_translate("MainWindow", "统计"))
        self.action_QT.setText(_translate("MainWindow", "关于QT"))
        self.action_12.setText(_translate("MainWindow", "关于软件"))

import my_icon_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
