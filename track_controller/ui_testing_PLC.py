# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\p214s\OneDrive\Documents\GitHub\Team_X_ECE_1140\track_controller\testing_PLC.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TestingWindow(object):
    def setupUi(self, TestingWindow):
        TestingWindow.setObjectName("TestingWindow")
        TestingWindow.resize(2163, 1334)
        self.centralwidget = QtWidgets.QWidget(TestingWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SwitchPosInput_Table = QtWidgets.QTableWidget(self.centralwidget)
        self.SwitchPosInput_Table.setGeometry(QtCore.QRect(0, 40, 541, 400))
        self.SwitchPosInput_Table.setRowCount(0)
        self.SwitchPosInput_Table.setColumnCount(2)
        self.SwitchPosInput_Table.setObjectName("SwitchPosInput_Table")
        item = QtWidgets.QTableWidgetItem()
        self.SwitchPosInput_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.SwitchPosInput_Table.setHorizontalHeaderItem(1, item)
        self.Suggested_Speed_Table = QtWidgets.QTableWidget(self.centralwidget)
        self.Suggested_Speed_Table.setGeometry(QtCore.QRect(1620, 40, 541, 400))
        self.Suggested_Speed_Table.setRowCount(0)
        self.Suggested_Speed_Table.setColumnCount(2)
        self.Suggested_Speed_Table.setObjectName("Suggested_Speed_Table")
        item = QtWidgets.QTableWidgetItem()
        self.Suggested_Speed_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Suggested_Speed_Table.setHorizontalHeaderItem(1, item)
        self.Occupancy_Table = QtWidgets.QTableWidget(self.centralwidget)
        self.Occupancy_Table.setGeometry(QtCore.QRect(540, 40, 541, 400))
        self.Occupancy_Table.setRowCount(0)
        self.Occupancy_Table.setColumnCount(2)
        self.Occupancy_Table.setObjectName("Occupancy_Table")
        item = QtWidgets.QTableWidgetItem()
        self.Occupancy_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Occupancy_Table.setHorizontalHeaderItem(1, item)
        self.SwitchPosOutput_Table = QtWidgets.QTableWidget(self.centralwidget)
        self.SwitchPosOutput_Table.setGeometry(QtCore.QRect(-10, 880, 551, 400))
        self.SwitchPosOutput_Table.setRowCount(0)
        self.SwitchPosOutput_Table.setColumnCount(2)
        self.SwitchPosOutput_Table.setObjectName("SwitchPosOutput_Table")
        item = QtWidgets.QTableWidgetItem()
        self.SwitchPosOutput_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.SwitchPosOutput_Table.setHorizontalHeaderItem(1, item)
        self.LightColor_Table = QtWidgets.QTableWidget(self.centralwidget)
        self.LightColor_Table.setGeometry(QtCore.QRect(540, 880, 541, 400))
        self.LightColor_Table.setRowCount(0)
        self.LightColor_Table.setColumnCount(2)
        self.LightColor_Table.setObjectName("LightColor_Table")
        item = QtWidgets.QTableWidgetItem()
        self.LightColor_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.LightColor_Table.setHorizontalHeaderItem(1, item)
        self.RailwayCrossing_Table = QtWidgets.QTableWidget(self.centralwidget)
        self.RailwayCrossing_Table.setGeometry(QtCore.QRect(1080, 880, 541, 400))
        self.RailwayCrossing_Table.setRowCount(0)
        self.RailwayCrossing_Table.setColumnCount(2)
        self.RailwayCrossing_Table.setObjectName("RailwayCrossing_Table")
        item = QtWidgets.QTableWidgetItem()
        self.RailwayCrossing_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RailwayCrossing_Table.setHorizontalHeaderItem(1, item)
        self.UploadNewPLCButton = QtWidgets.QPushButton(self.centralwidget)
        self.UploadNewPLCButton.setGeometry(QtCore.QRect(900, 490, 371, 51))
        self.UploadNewPLCButton.setObjectName("UploadNewPLCButton")
        self.CurrentPLCLabel = QtWidgets.QLabel(self.centralwidget)
        self.CurrentPLCLabel.setGeometry(QtCore.QRect(580, 640, 1031, 41))
        self.CurrentPLCLabel.setObjectName("CurrentPLCLabel")
        self.run_PLC_button = QtWidgets.QPushButton(self.centralwidget)
        self.run_PLC_button.setGeometry(QtCore.QRect(900, 770, 371, 51))
        self.run_PLC_button.setObjectName("run_PLC_button")
        self.Commanded_Speed_Table = QtWidgets.QTableWidget(self.centralwidget)
        self.Commanded_Speed_Table.setGeometry(QtCore.QRect(1620, 880, 541, 400))
        self.Commanded_Speed_Table.setRowCount(0)
        self.Commanded_Speed_Table.setColumnCount(2)
        self.Commanded_Speed_Table.setObjectName("Commanded_Speed_Table")
        item = QtWidgets.QTableWidgetItem()
        self.Commanded_Speed_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Commanded_Speed_Table.setHorizontalHeaderItem(1, item)
        self.Authority_Table = QtWidgets.QTableWidget(self.centralwidget)
        self.Authority_Table.setGeometry(QtCore.QRect(1080, 40, 541, 400))
        self.Authority_Table.setRowCount(0)
        self.Authority_Table.setColumnCount(2)
        self.Authority_Table.setObjectName("Authority_Table")
        item = QtWidgets.QTableWidgetItem()
        self.Authority_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Authority_Table.setHorizontalHeaderItem(1, item)
        self.Status_Table = QtWidgets.QTableWidget(self.centralwidget)
        self.Status_Table.setGeometry(QtCore.QRect(-10, 460, 551, 400))
        self.Status_Table.setRowCount(0)
        self.Status_Table.setColumnCount(2)
        self.Status_Table.setObjectName("Status_Table")
        item = QtWidgets.QTableWidgetItem()
        self.Status_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Status_Table.setHorizontalHeaderItem(1, item)
        self.speed_limit_table = QtWidgets.QTableWidget(self.centralwidget)
        self.speed_limit_table.setGeometry(QtCore.QRect(1620, 460, 551, 400))
        self.speed_limit_table.setRowCount(0)
        self.speed_limit_table.setColumnCount(2)
        self.speed_limit_table.setObjectName("speed_limit_table")
        item = QtWidgets.QTableWidgetItem()
        self.speed_limit_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.speed_limit_table.setHorizontalHeaderItem(1, item)
        self.ErrorBoxLabel = QtWidgets.QLabel(self.centralwidget)
        self.ErrorBoxLabel.setGeometry(QtCore.QRect(580, 580, 1021, 31))
        self.ErrorBoxLabel.setObjectName("ErrorBoxLabel")
        TestingWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TestingWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2163, 22))
        self.menubar.setObjectName("menubar")
        TestingWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TestingWindow)
        self.statusbar.setObjectName("statusbar")
        TestingWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TestingWindow)
        QtCore.QMetaObject.connectSlotsByName(TestingWindow)

    def retranslateUi(self, TestingWindow):
        _translate = QtCore.QCoreApplication.translate
        TestingWindow.setWindowTitle(_translate("TestingWindow", "Testing Window"))
        item = self.SwitchPosInput_Table.horizontalHeaderItem(0)
        item.setText(_translate("TestingWindow", "Block Number"))
        item = self.SwitchPosInput_Table.horizontalHeaderItem(1)
        item.setText(_translate("TestingWindow", "Switch Position"))
        item = self.Suggested_Speed_Table.horizontalHeaderItem(0)
        item.setText(_translate("TestingWindow", "Block Number"))
        item = self.Suggested_Speed_Table.horizontalHeaderItem(1)
        item.setText(_translate("TestingWindow", "Suggested Speed"))
        item = self.Occupancy_Table.horizontalHeaderItem(0)
        item.setText(_translate("TestingWindow", "Block Number"))
        item = self.Occupancy_Table.horizontalHeaderItem(1)
        item.setText(_translate("TestingWindow", "Occupancy"))
        item = self.SwitchPosOutput_Table.horizontalHeaderItem(0)
        item.setText(_translate("TestingWindow", "Block Number"))
        item = self.SwitchPosOutput_Table.horizontalHeaderItem(1)
        item.setText(_translate("TestingWindow", "Switch Position"))
        item = self.LightColor_Table.horizontalHeaderItem(0)
        item.setText(_translate("TestingWindow", "Block Number"))
        item = self.LightColor_Table.horizontalHeaderItem(1)
        item.setText(_translate("TestingWindow", "Light Colors"))
        item = self.RailwayCrossing_Table.horizontalHeaderItem(0)
        item.setText(_translate("TestingWindow", "Block Number"))
        item = self.RailwayCrossing_Table.horizontalHeaderItem(1)
        item.setText(_translate("TestingWindow", "Railway Crossing"))
        self.UploadNewPLCButton.setText(_translate("TestingWindow", "Upload New PLC"))
        self.CurrentPLCLabel.setText(_translate("TestingWindow", "Currently Running PLC: "))
        self.run_PLC_button.setText(_translate("TestingWindow", "Run PLC"))
        item = self.Commanded_Speed_Table.horizontalHeaderItem(0)
        item.setText(_translate("TestingWindow", "Block Number"))
        item = self.Commanded_Speed_Table.horizontalHeaderItem(1)
        item.setText(_translate("TestingWindow", "Command Speed"))
        item = self.Authority_Table.horizontalHeaderItem(0)
        item.setText(_translate("TestingWindow", "Block Number"))
        item = self.Authority_Table.horizontalHeaderItem(1)
        item.setText(_translate("TestingWindow", "Authority"))
        item = self.Status_Table.horizontalHeaderItem(0)
        item.setText(_translate("TestingWindow", "Block Number"))
        item = self.Status_Table.horizontalHeaderItem(1)
        item.setText(_translate("TestingWindow", "Status"))
        item = self.speed_limit_table.horizontalHeaderItem(0)
        item.setText(_translate("TestingWindow", "Block Number"))
        item = self.speed_limit_table.horizontalHeaderItem(1)
        item.setText(_translate("TestingWindow", "Speed Limit"))
        self.ErrorBoxLabel.setText(_translate("TestingWindow", " "))
