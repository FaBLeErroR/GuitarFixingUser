from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidgetItem
from PySide6.QtSql import QSqlTableModel
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtUiTools import QUiLoader
import sys
from Ui.ui_userMain import Ui_MainWindow
from Ui.ui_userRepair import Ui_Dialog as ActionsShow

from connection import Data

class MainWindow(QMainWindow, Ui_MainWindow, Data):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setupUi(self)
        self.conn = Data()

        #Sidebar
        self.choose_diagnostic.clicked.connect(self.to_choose_diagnostic_page)
        self.choose_parrameters.clicked.connect(self.to_choose_parameters_page)
        self.repair_plan_update.clicked.connect(self.view_reair)
        self.action_tablice_update.clicked.connect(self.view_actions)
        self.find_diagnostic_button.clicked.connect(self.get_characteristic_data)
        self.find_repairs_button.clicked.connect(self.get_repairs)
        self.go_to_repair.clicked.connect(self.open_actions_window)

        #Details page        
        # self.add_detail.clicked.connect(self.open_add_detail_window)
        # self.edit__detail.clicked.connect(self.open_add_detail_window)
        # self.delite_detail.clicked.connect(self.delete_detail_click)


        # Updating tablices
        # if self.stackedWidget.currentIndex == 2:
        #     self.view_actions()
        # elif self.stackedWidget.currentIndex == 4:
        #     self.view_characteristics()
        # elif self.stackedWidget.currentIndex == 1:
        #     self.view_diagnostic()
        # else:
        #     self.view_detail()


    #Sidebar functions
    def to_choose_diagnostic_page(self):
        self.stackedWidget.setCurrentIndex(0)
        self.view_diagnostic()

    def to_choose_parameters_page(self):
        self.stackedWidget.setCurrentIndex(1)
        # self.make_characteristic_table()

    def view_diagnostic(self):
        self.choose_diagnostc_list.clear()
        self.choose_diagnostc_list.addItems(self.get_diagnostic()) 

    def view_reair(self):
        self.choose_repair_plan_list.clear()
        curent_diagnostic = self.choose_diagnostc_list.currentText()
        # self.choose_repair_plan_list.clear()
        self.choose_repair_plan_list.addItems(self.get_repair(curent_diagnostic))

    # def make_characteristic_table(self):
    #     self.chatacteristics_table.setColumnCount(self.chatacteristics_table.columnCount() + 2)
    #     self.chatacteristics_table.setHorizontalHeaderLabels(["Характеристика", "Значение"] + [self.chatacteristics_table.horizontalHeaderItem(col).text() for col in range(self.chatacteristics_table.columnCount()-2)])

    #     # Добавление пустых ячеек в новые столбцы
    #     self.add_empty_columns(6)

    # def add_empty_columns(self, count):
    #     for i in range(count):
    #         rowPosition = self.chatacteristics_table.rowCount()
    #         self.chatacteristics_table.insertRow(rowPosition)

    def get_characteristic_data(self):
        data = []
        for row in range(self.chatacteristics_table.rowCount()):
            characteristic = self.chatacteristics_table.item(row, 0)
            characteristic = characteristic.text() if characteristic is not None else ""
            value = self.chatacteristics_table.item(row, 1)
            value = value.text() if value is not None else ""
            if value != '' and characteristic != '':
                data.append([characteristic, value])
        if len(data) > 0:
            self.choose_diagnostc_par_list.clear()
            self.choose_diagnostc_par_list.addItems(self.get_diagnostic_by_table(data)) 

    def get_repairs(self):
        self.choose_repair_plan_par_list.clear()
        curent_diagnostic = self.choose_diagnostc_par_list.currentText()
        # self.choose_repair_plan_list.clear()
        self.choose_repair_plan_par_list.addItems(self.get_repair(curent_diagnostic))
        
    def open_actions_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_actions = ActionsShow()
        self.ui_actions.setupUi(self.new_window)
        self.new_window.show()

        self.model = QSqlTableModel(self)
        repair_name = self.choose_repair_plan_par_list.currentText()
        self.model.setQuery(f'''SELECT Action.step, Action.action_name
                            FROM Action
                            JOIN Repair ON Action.repair_id = Repair.repair_id
                            WHERE Repair.repair_name = '{repair_name}'
                            ORDER BY Action.step;''')
        self.model.select()
        self.ui_actions.repair_table_alone.setModel(self.model)

    def view_actions(self):
        self.model = QSqlTableModel(self)
        repair_name = self.choose_repair_plan_list.currentText()
        self.model.setQuery(f'''SELECT Action.step, Action.action_name
                            FROM Action
                            JOIN Repair ON Action.repair_id = Repair.repair_id
                            WHERE Repair.repair_name = '{repair_name}'
                            ORDER BY Action.step;''')
        self.model.select()
        self.repairs_table.setModel(self.model)