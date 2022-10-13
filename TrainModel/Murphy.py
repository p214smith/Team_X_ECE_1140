from PyQt6.QtWidgets import QApplication, QWidget, QFrame, QDialog, QGridLayout, QAbstractItemView
from PyQt6.QtWidgets import QLabel, QPushButton, QRadioButton, QSlider, QSizePolicy, QTableWidget, QTableView, QAbstractItemView, QHeaderView
from PyQt6.QtCore import Qt, QRect, QTimer, QSortFilterProxyModel
from PyQt6.QtGui import QFont, QStandardItemModel, QStandardItem
from Test import TestUI
from FontStyles import *
from common import *
    
class MurphyUI(QFrame):
    def __init__(self):
        #Initialize parent class
        super().__init__()

        #Set up some basic window settings
        self.setGeometry(100,100, 500, 600)
        self.setWindowTitle("Train Model")
        self.setAttribute(Qt.WidgetAttribute.WA_AlwaysShowToolTips, True)

        #Declare labels & buttons
        self.testing_button = QPushButton("Test This Module...");
        self.train_info_select_label = QLabel("Train Information & Selection");
        self.train_info_select_table = QTableView()
        self.failure_generation_label = QLabel("Failure Generation");
        self.engine_failure_button = QPushButton("Generate Engine Failure for Selected Train");
        self.signal_pickup_failure_button = QPushButton("Generate Signal Pickup Failure for Selected Train");
        self.brake_failure_button = QPushButton("Generate Brake Failure for Selected Train");
        self.random_failure_generation_label = QLabel("Random Train Failure Generation");
        self.radiobuttonOff = QRadioButton("Off")
        self.radiobuttonOn = QRadioButton("On")
        self.random_engine_generation_label = QLabel("Number of Engine Failures per Train per Hour: ");
        self.random_engine_generation_slider = QSlider(Qt.Orientation.Horizontal)
        self.random_engine_generation_value = QLabel("0.0");
        self.random_signal_generation_label = QLabel("Number of Signal Pickup Failures per Train per Hour: ");
        self.random_signal_generation_slider = QSlider(Qt.Orientation.Horizontal)
        self.random_signal_generation_value = QLabel("0.0");
        self.random_brake_generation_label = QLabel("Number of Brake Failures per Train per Hour: ");
        self.random_brake_generation_slider = QSlider(Qt.Orientation.Horizontal)
        self.random_brake_generation_value = QLabel("0.0");
            
        #Set up button functions
        self.testing_button.clicked.connect(self.test_launch)
        self.engine_failure_button.clicked.connect(self.generate_engine_failure)
        self.signal_pickup_failure_button.clicked.connect(self.generate_signal_failure)
        self.brake_failure_button.clicked.connect(self.generate_brake_failure)

        #Set up the table settings
        train_proxy_model.setSourceModel(train_info_model)
        self.train_info_select_table.setModel(train_proxy_model)
        train_info_model.setHorizontalHeaderLabels(['Train ID', 'Velocity\n(MPH)', 'Distance\n(Feet)', 'Commanded Engine Power\n(Watts)', 'Braking', 
                                                                'Track Grade\n(°)', 'Passenger Count', 'Fault(s)', 'Interior Temperature\n(Fahrenheit)',
                                                                'Interior Lights\n(On/Off)', 'Exterior Lights\n(On/Off)', 'Left Doors\n(Open/Closed)', 'Right Doors\n(Open/Closed)'])

        #Hide all the columns except the ID and Faults
        self.train_info_select_table.setColumnHidden(1, True)
        self.train_info_select_table.setColumnHidden(2, True)
        self.train_info_select_table.setColumnHidden(3, True)
        self.train_info_select_table.setColumnHidden(4, True)
        self.train_info_select_table.setColumnHidden(5, True)
        self.train_info_select_table.setColumnHidden(6, True)
        self.train_info_select_table.setColumnHidden(8, True)
        self.train_info_select_table.setColumnHidden(9, True)
        self.train_info_select_table.setColumnHidden(10, True)
        self.train_info_select_table.setColumnHidden(11, True)
        self.train_info_select_table.setColumnHidden(12, True)

        self.train_info_select_table.verticalHeader().hide()
        self.train_info_select_table.setSortingEnabled(True)
        self.train_info_select_table.horizontalHeader().setStretchLastSection(True)
        self.train_info_select_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows); 
        self.train_info_select_table.horizontalHeader().setHighlightSections(False);
        self.train_info_select_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.train_info_select_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers);

        #Set label fonts & buttons
        self.testing_button.setFont(small_font)
        self.train_info_select_label.setFont(section_font);
        self.train_info_select_table.setFont(normal_font);
        self.train_info_select_table.horizontalHeader().setFont(normal_font);
        self.train_info_select_table.verticalHeader().setFont(normal_font);
        self.failure_generation_label.setFont(section_font);
        self.engine_failure_button.setFont(normal_font);
        self.signal_pickup_failure_button.setFont(normal_font);
        self.brake_failure_button.setFont(normal_font);
        self.random_failure_generation_label.setFont(section_font);
        self.radiobuttonOff.setFont(normal_font);
        self.radiobuttonOn.setFont(normal_font);
        self.random_engine_generation_label.setFont(normal_font)
        self.random_engine_generation_value.setFont(normal_font)
        self.random_signal_generation_label.setFont(normal_font)
        self.random_signal_generation_value.setFont(normal_font)
        self.random_brake_generation_label.setFont(normal_font)
        self.random_brake_generation_value.setFont(normal_font)

        #Color labels & buttons
        self.testing_button.setStyleSheet(gold_button_stylesheet)
        self.train_info_select_label.setStyleSheet(section_label_stylesheet)
        self.train_info_select_table.setStyleSheet(table_stylesheet)
        self.train_info_select_table.setAlternatingRowColors(True);
        self.failure_generation_label.setStyleSheet(section_label_stylesheet)
        self.engine_failure_button.setStyleSheet(red_button_stylesheet)
        self.signal_pickup_failure_button.setStyleSheet(red_button_stylesheet)
        self.brake_failure_button.setStyleSheet(red_button_stylesheet)
        self.random_failure_generation_label.setStyleSheet(section_label_stylesheet)
        self.radiobuttonOff.setStyleSheet(radio_stylesheet)
        self.radiobuttonOn.setStyleSheet(radio_stylesheet)
        self.random_engine_generation_label.setStyleSheet(normal_label_stylesheet)
        self.random_engine_generation_value.setStyleSheet(normal_label_stylesheet)
        self.random_signal_generation_label.setStyleSheet(normal_label_stylesheet)
        self.random_signal_generation_value.setStyleSheet(normal_label_stylesheet)
        self.random_brake_generation_label.setStyleSheet(normal_label_stylesheet)
        self.random_brake_generation_value.setStyleSheet(normal_label_stylesheet)

        #Connect Radio Button Functionality
        self.radiobuttonOff.clicked.connect(self.radioButtonClicked)
        self.radiobuttonOn.clicked.connect(self.radioButtonClicked)

        #Set Slider Ranges
        self.random_engine_generation_slider.setMinimum(0)
        self.random_engine_generation_slider.setMaximum(100)

        self.random_signal_generation_slider.setMinimum(0)
        self.random_signal_generation_slider.setMaximum(100)

        self.random_brake_generation_slider.setMinimum(0)
        self.random_brake_generation_slider.setMaximum(100)

        #Make sliders update labels
        self.random_engine_generation_slider.valueChanged.connect(self.random_engine_failure_update)
        self.random_signal_generation_slider.valueChanged.connect(self.random_signal_failure_update)
        self.random_brake_generation_slider.valueChanged.connect(self.random_brake_failure_update)

        #Make the buttons as small as possible
        self.testing_button.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        self.engine_failure_button.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        self.signal_pickup_failure_button.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        self.brake_failure_button.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)

        #Set the random train generation off by default
        self.radiobuttonOff.setChecked(True)

        #Declare the grid and add the necessary widgets to it
        murphy_grid = QGridLayout()
        murphy_grid.addWidget(self.testing_button, 0, 0, 1, 4, alignment=Qt.AlignmentFlag.AlignCenter)
        murphy_grid.addWidget(self.train_info_select_label, 1, 0, 1, 4, alignment=Qt.AlignmentFlag.AlignCenter)
        murphy_grid.addWidget(self.train_info_select_table, 2, 0, 1, 4, alignment=Qt.AlignmentFlag.AlignCenter)
        murphy_grid.addWidget(self.failure_generation_label, 3, 0, 1, 4, alignment=Qt.AlignmentFlag.AlignCenter)
        murphy_grid.addWidget(self.engine_failure_button, 4, 0, 1, 4, alignment=Qt.AlignmentFlag.AlignCenter)
        murphy_grid.addWidget(self.signal_pickup_failure_button, 5, 0, 1, 4, alignment=Qt.AlignmentFlag.AlignCenter)
        murphy_grid.addWidget(self.brake_failure_button, 6, 0, 1, 4, alignment=Qt.AlignmentFlag.AlignCenter)
        murphy_grid.addWidget(self.random_failure_generation_label, 7, 0, 1, 4, alignment=Qt.AlignmentFlag.AlignCenter)
        murphy_grid.addWidget(self.radiobuttonOff, 8, 0, 1, 1, alignment=Qt.AlignmentFlag.AlignRight)
        murphy_grid.addWidget(self.radiobuttonOn, 8, 1, 1, 1, alignment=Qt.AlignmentFlag.AlignRight)
        murphy_grid.addWidget(self.random_engine_generation_label, 9, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignRight)
        murphy_grid.addWidget(self.random_engine_generation_slider, 9, 2, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        murphy_grid.addWidget(self.random_engine_generation_value, 9, 3, 1, 1, alignment=Qt.AlignmentFlag.AlignLeft)
        murphy_grid.addWidget(self.random_signal_generation_label, 10, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignRight)
        murphy_grid.addWidget(self.random_signal_generation_slider, 10, 2, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        murphy_grid.addWidget(self.random_signal_generation_value, 10, 3, 1, 1, alignment=Qt.AlignmentFlag.AlignLeft)
        murphy_grid.addWidget(self.random_brake_generation_label, 11, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignRight)
        murphy_grid.addWidget(self.random_brake_generation_slider, 11, 2, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        murphy_grid.addWidget(self.random_brake_generation_value, 11, 3, 1, 1, alignment=Qt.AlignmentFlag.AlignLeft)

        #Disable widgets that should be disabled on startup
        self.random_engine_generation_label.setEnabled(False)
        self.random_engine_generation_slider.setEnabled(False)
        self.random_engine_generation_value.setEnabled(False)

        self.random_signal_generation_label.setEnabled(False)
        self.random_signal_generation_slider.setEnabled(False)
        self.random_signal_generation_value.setEnabled(False)

        self.random_brake_generation_label.setEnabled(False)
        self.random_brake_generation_slider.setEnabled(False)
        self.random_brake_generation_value.setEnabled(False)

        #Set up the window color pallete
        self.setObjectName("MurphyWindow")
        self.setStyleSheet('''#MurphyWindow {background-color: rgb(102,102,102); border: 3px solid black;}''')

        #Connect the grid, and show the window
        self.setLayout(murphy_grid);

    def generate_brake_failure(self):
        try:
            #First, get the selected ID
            ID = int(train_proxy_model.data(train_proxy_model.index(self.train_info_select_table.selectedIndexes()[0].row(), 0)))

            #Throw up a warning window to make sure it wasn't a misclick
            if not my_warning(msg = "Are you sure you want to generate a brake\nfailure for Train " + str(ID) + "?", title = "Failure Generation Confirmation", parent = self).exec(): return
            
            #Next, update the actual train
            handler.train_list[handler.get_train_from_ID(ID)].generate_brake_failure()

            #Finally, update the table
            for i in range(train_info_model.rowCount()):
                if int(train_info_model.item(i, 0).text()) == ID:
                    train_info_model.setItem(i, 7, QStandardItem("Brake Failure")) 

            #Show a confirmation message to the user
            my_message(msg = "Brake failure successfully generated for Train " + str(ID) + "!", title = "Brake Failure Generated", error = False, parent = self).exec()

        #If there is an index error, then there is no selection, and we should throw up an error
        except IndexError:
            my_message(msg = "You have not selected a train!\nPlease select a train and try again.", title = "No Train Selected", error = True, parent = self).exec()
           

    def generate_engine_failure(self):
        try:
            #First, get the selected ID
            ID = int(train_proxy_model.data(train_proxy_model.index(self.train_info_select_table.selectedIndexes()[0].row(), 0)))

            #Throw up a warning window to make sure it wasn't a misclick
            if not my_warning(msg = "Are you sure you want to generate an engine\nfailure for Train " + str(ID) + "?", title = "Failure Generation Confirmation", parent = self).exec(): return
            
            #Next, update the actual train
            handler.train_list[handler.get_train_from_ID(ID)].generate_engine_failure()

            #Finally, update the table
            for i in range(train_info_model.rowCount()):
                if int(train_info_model.item(i, 0).text()) == ID:
                    train_info_model.setItem(i, 7, QStandardItem("Engine Failure"))
            
            #Show a confirmation message to the user
            my_message(msg = "Engine failure successfully generated for Train " + str(ID) + "!", title = "Engine Failure Generated", error = False, parent = self).exec()

        #If there is an index error, then there is no selection, and we should throw up an error
        except IndexError:
            my_message(msg = "You have not selected a train!\nPlease select a train and try again.", title = "No Train Selected", error = True, parent = self).exec()

    def generate_signal_failure(self):
        try:
            #First, get the selected ID
            ID = int(train_proxy_model.data(train_proxy_model.index(self.train_info_select_table.selectedIndexes()[0].row(), 0)))
            
            #Throw up a warning window to make sure it wasn't a misclick
            if not my_warning(msg = "Are you sure you want to generate a signal\npickup failure for Train " + str(ID) + "?", title = "Failure Generation Confirmation", parent = self).exec(): return
            
            #Next, update the actual train
            handler.train_list[handler.get_train_from_ID(ID)].generate_signal_pickup_failure()

            #Finally, update the table
            for i in range(train_info_model.rowCount()):
                if int(train_info_model.item(i, 0).text()) == ID:
                    train_info_model.setItem(i, 7, QStandardItem("Signal Pickup Failure"))

            #Show a confirmation message to the user
            my_message(msg = "Signal pickup failure successfully generated for Train " + str(ID) + "!", title = "Signal Pickup Failure Generated", error = False, parent = self).exec()

        #If there is an index error, then there is no selection, and we should throw up an error
        except IndexError:
            my_message(msg = "You have not selected a train!\nPlease select a train and try again.", title = "No Train Selected", error = True, parent = self).exec()

    #This function launches the test UI
    def test_launch(self):
        if(my_warning("Are you sure that you want to launch the testing windows? \n         (All other activity will be stopped while testing)", title = "Test Launch Confirmation", parent = murphy_window).exec()):
            self.my_Test_UI = TestUI()
            self.my_Test_UI.show()

    #These functions update the slider labels
    def random_engine_failure_update(self, value):
        self.random_engine_generation_value.setText(str(value/100.0))

    def random_signal_failure_update(self, value):
        self.random_signal_generation_value.setText(str(value/100.0))

    def random_brake_failure_update(self, value):
        self.random_brake_generation_value.setText(str(value/100.0))

    #This function enables/disables sliders
    def radioButtonClicked(self):
        self.random_engine_generation_label.setEnabled(self.radiobuttonOn.isChecked())
        self.random_engine_generation_slider.setEnabled(self.radiobuttonOn.isChecked())
        self.random_engine_generation_value.setEnabled(self.radiobuttonOn.isChecked())

        self.random_signal_generation_label.setEnabled(self.radiobuttonOn.isChecked())
        self.random_signal_generation_slider.setEnabled(self.radiobuttonOn.isChecked())
        self.random_signal_generation_value.setEnabled(self.radiobuttonOn.isChecked())

        self.random_brake_generation_label.setEnabled(self.radiobuttonOn.isChecked())
        self.random_brake_generation_slider.setEnabled(self.radiobuttonOn.isChecked())
        self.random_brake_generation_value.setEnabled(self.radiobuttonOn.isChecked())
            
#dlg = my_message("You have not selected a train!\nPlease select a train and try again.", title = "No Train Selected", parent = murphy_window)
#dlg.exec()

#dlg = my_warning("Are you sure you want to generate a brake failure for Train 8?", title = "Failure Generation Confirmation", parent = murphy_window)
#print(dlg.exec())

#Set up the Qapp and murphy window
app = QApplication([])
murphy_window = MurphyUI()

#Show the murphy window
murphy_window.show()

#Start the event loop
app.exec()