import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
from track_control_controller import track_control_controller
import copy
from track_controller import WaysideController

TestingPLCWind = "testing_PLC.ui"
Ui_TestingWindow, QtBaseClass = uic.loadUiType("track_controller/"+TestingPLCWind)

class test_window (QtWidgets.QMainWindow, Ui_TestingWindow):
    def __init__(self, trc):
        self.track_control_data = copy.copy(trc)
        QtWidgets.QMainWindow.__init__(self)
        Ui_TestingWindow.__init__(self)
        self.setupUi(self)
        self.UploadNewPLCButton.clicked.connect(self.openFileNameDialog)
        self.run_PLC_button.clicked.connect(self.run_plc)

        self.CurrentPLCLabel.setText("Currently Running: "+ self.track_control_data.get_PLC())

        self.SwitchPosInput_Table.itemChanged.connect(self.item_changed)
        self.Authority_Table.itemChanged.connect(self.item_changed)
        self.Occupancy_Table.itemChanged.connect(self.item_changed)

        cspeed = self.track_control_data.get_commanded_speed()
        #self.commanded_speed_label.setText("Commanded Speed: "+ str(cspeed))

        self.update_tables()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            self.track_data.set_PLC(filename)
            self.CurrentPLCLabel.setText("Currently Running: "+ fileName)
    
    def item_changed(self, item):
        if item.column() ==1:
            if item.data(0) == "F" or item.data(0) == "f" or item.data(0) == "0":
                item.setText( "False" )
            elif item.data(0) == "T" or item.data(0) == "t" or item.data(0) == "1":
                item.setText( "True" )

    def update_tables(self):
        self.update_table(self.track_control_data.get_switch_positions(), self.SwitchPosInput_Table, True)
        self.update_table(self.track_control_data.get_authority(), self.Authority_Table, True)
        self.update_table(self.track_control_data.get_suggested_speed(), self.Suggested_Speed_Table, True)
        self.update_table(self.track_control_data.get_occupancy(), self.Occupancy_Table, True)
        self.update_table(self.track_control_data.get_switch_positions(), self.SwitchPosOutput_Table, False)
        self.update_light_table(self.track_control_data.get_light_colors(), self.LightColor_Table, False)
        self.update_table(self.track_control_data.get_railway_crossings(), self.RailwayCrossing_Table, False)
        self.update_table(self.track_control_data.get_commanded_speed(), self.Commanded_Speed_Table, False)
        
    def update_table(self, data, table, changable):
        numrows = len(data)
        table.setRowCount(numrows)
        for row in range(numrows):
            for column in range(2):
                item = QTableWidgetItem(str(data[row][column]))
                if not(changable) or column==0 :
                    item.setFlags(QtCore.Qt.ItemIsEditable)
                table.setItem(row, column, item)

    def update_light_table(self, data, table, changable):
        numrows = len(data)
        table.setRowCount(numrows)
        for row in range(numrows):
            for column in range(2):
                if(column == 1):
                    if(data[row][column] and data[row][column+1]):
                        item = QTableWidgetItem("Green")
                    elif(data[row][column] or data[row][column+1]):
                        item = QTableWidgetItem("Yellow")
                    else:
                        item = QTableWidgetItem("Red")
                else:
                    item = QTableWidgetItem(str(data[row][column]))
                if not(changable) or column==0 :
                    item.setFlags(QtCore.Qt.ItemIsEditable)
                table.setItem(row, column, item)

    def run_plc (self):
        self.make_changes()
        self.track_control_data.ParsePLC()
        self.update_tables()

    def make_changes(self):
        self.get_table_change(self.track_control_data.get_switch_positions(), self.SwitchPosInput_Table)
        self.get_table_change(self.track_control_data.get_suggested_speed(), self.Suggested_Speed_Table)
        self.get_table_change(self.track_control_data.get_authority(), self.Authority_Table)
        self.get_table_change(self.track_control_data.get_occupancy(), self.Occupancy_Table)
        self.update_tables()

    def get_table_change (self, table_data, table):
        rowC = table.rowCount()
        for row in range(rowC):
            for dat_row in range(rowC):
                (block, state) = table_data[dat_row]
                if str(block) == table.item(row, 0).data(0):
                    table_data[dat_row] = (block, table.item(row, 1).data(0))

trackTest = WaysideController()
trackTest.set_authority([(1,True), (2, False), (3, False)])
trackTest.set_switch_positions([(1,True), (2, True), (3, False)])
trackTest.set_occupancy([(1,True), (2, True), (4, False)])
trackTest.set_railway_crossings([(1,True), (2, True), (3, False)])
trackTest.set_light_colors([(1,True,True), (5, True,True), (3, False,True)])
trackTest.set_statuses([(1,True), (2, True), (3, True)])
trackTest.set_suggested_speed([(1,0b00011010), (2, 0b00100111), (3, 0b00010101)])
trackTest.set_commanded_speed([(1,0b000000010), (2, 0b00100000), (3, 0b00000100)])
trackTest.set_PLC("track_controller/testPLCfile.txt")
app = QtWidgets.QApplication(sys.argv)
window = test_window(trackTest)
window.show()
app.exec_()