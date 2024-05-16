# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_user.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QTableView,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 500)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 110, 780, 380))
        self.chose_diagnostic_field = QWidget()
        self.chose_diagnostic_field.setObjectName(u"chose_diagnostic_field")
        self.chose_diagnostic_field.setStyleSheet(u"Line{\n"
"	background-color: #ffb146;\n"
"	border: none;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: #ff9f1b;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	background-color: #f1d275;\n"
"	border: 1px solid #ffad3d;\n"
"	height: 30px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #ff9d16;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #ff9d16;\n"
"}\n"
"\n"
"QComboBox {\n"
"	border: 1px solid #ffad3d;\n"
"	font-size: 14pt;\n"
"}\n"
"\n"
"QTableView{\n"
"	border: 1px solid #ffad3d;\n"
"}\n"
"\n"
"QTableView::item{\n"
"	border: 1px solid #ffad3d;\n"
"	color: #ffa120;\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	background-color: #ffad3d;\n"
"	color: white;\n"
"}\n"
"\n"
"QHeaderView{\n"
"	width:100%;\n"
"	background-color: #ffa120;\n"
"	color: white;\n"
"	border: none;\n"
"	font-weight: bold;\n"
"	padding: 2px;\n"
"}")
        self.diagnostic_data = QWidget(self.chose_diagnostic_field)
        self.diagnostic_data.setObjectName(u"diagnostic_data")
        self.diagnostic_data.setGeometry(QRect(0, 0, 780, 380))
        self.diagn = QWidget(self.diagnostic_data)
        self.diagn.setObjectName(u"diagn")
        self.diagn.setGeometry(QRect(0, 0, 780, 380))
        self.verticalLayout = QVBoxLayout(self.diagn)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.choose_diagnostc_list = QComboBox(self.diagn)
        self.choose_diagnostc_list.setObjectName(u"choose_diagnostc_list")
        font = QFont()
        font.setPointSize(14)
        self.choose_diagnostc_list.setFont(font)
        self.choose_diagnostc_list.setEditable(False)

        self.verticalLayout.addWidget(self.choose_diagnostc_list)

        self.choose_repair_plan_list = QComboBox(self.diagn)
        self.choose_repair_plan_list.setObjectName(u"choose_repair_plan_list")
        self.choose_repair_plan_list.setFont(font)

        self.verticalLayout.addWidget(self.choose_repair_plan_list)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.repair_plan_update = QPushButton(self.diagn)
        self.repair_plan_update.setObjectName(u"repair_plan_update")

        self.horizontalLayout_2.addWidget(self.repair_plan_update)

        self.action_tablice_update = QPushButton(self.diagn)
        self.action_tablice_update.setObjectName(u"action_tablice_update")

        self.horizontalLayout_2.addWidget(self.action_tablice_update)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.repairs_table = QTableView(self.diagn)
        self.repairs_table.setObjectName(u"repairs_table")
        self.repairs_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.repairs_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.repairs_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.repairs_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.repairs_table.horizontalHeader().setCascadingSectionResizes(True)
        self.repairs_table.horizontalHeader().setStretchLastSection(True)
        self.repairs_table.verticalHeader().setVisible(False)
        self.repairs_table.verticalHeader().setHighlightSections(False)

        self.verticalLayout.addWidget(self.repairs_table)

        self.stackedWidget.addWidget(self.chose_diagnostic_field)
        self.parameters_repair = QWidget()
        self.parameters_repair.setObjectName(u"parameters_repair")
        self.parameters_repair.setStyleSheet(u"Line{\n"
"	background-color: #ffb146;\n"
"	border: none;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: #ff9f1b;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	background-color: #f1d275;\n"
"	border: 1px solid #ffad3d;\n"
"	height: 30px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #ff9d16;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #ff9d16;\n"
"}\n"
"\n"
"QTableView{\n"
"	border: 1px solid #ffad3d;\n"
"}\n"
"\n"
"QTableView::item{\n"
"	border: 1px solid #ffad3d;\n"
"	color: #ffa120;\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	background-color: #ffad3d;\n"
"	color: white;\n"
"}\n"
"\n"
"QHeaderView{\n"
"	width:100%;\n"
"	background-color: #ffa120;\n"
"	color: white;\n"
"	border: none;\n"
"	font-weight: bold;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"\n"
"QComboBox {\n"
"	border: 1px solid #ffad3d;\n"
"	font-size: 14pt;\n"
"}\n"
"\n"
"QComboBox {\n"
"	border: 1px solid #ffad3d;\n"
"	font-size: 14pt;\n"
"}")
        self.buttons = QWidget(self.parameters_repair)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setGeometry(QRect(0, 340, 780, 31))
        self.horizontalLayout_3 = QHBoxLayout(self.buttons)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.find_diagnostic_button = QPushButton(self.buttons)
        self.find_diagnostic_button.setObjectName(u"find_diagnostic_button")
        self.find_diagnostic_button.setCheckable(True)
        self.find_diagnostic_button.setChecked(False)

        self.horizontalLayout_3.addWidget(self.find_diagnostic_button)

        self.find_repairs_button = QPushButton(self.buttons)
        self.find_repairs_button.setObjectName(u"find_repairs_button")

        self.horizontalLayout_3.addWidget(self.find_repairs_button)

        self.go_to_repair = QPushButton(self.buttons)
        self.go_to_repair.setObjectName(u"go_to_repair")

        self.horizontalLayout_3.addWidget(self.go_to_repair)

        self.choose_characteristic_data = QWidget(self.parameters_repair)
        self.choose_characteristic_data.setObjectName(u"choose_characteristic_data")
        self.choose_characteristic_data.setGeometry(QRect(0, 0, 780, 330))
        self.verticalLayout_2 = QVBoxLayout(self.choose_characteristic_data)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.choose_diagnostc_par_list = QComboBox(self.choose_characteristic_data)
        self.choose_diagnostc_par_list.setObjectName(u"choose_diagnostc_par_list")
        self.choose_diagnostc_par_list.setFont(font)
        self.choose_diagnostc_par_list.setEditable(False)

        self.verticalLayout_2.addWidget(self.choose_diagnostc_par_list)

        self.choose_repair_plan_par_list = QComboBox(self.choose_characteristic_data)
        self.choose_repair_plan_par_list.setObjectName(u"choose_repair_plan_par_list")
        self.choose_repair_plan_par_list.setFont(font)

        self.verticalLayout_2.addWidget(self.choose_repair_plan_par_list)

        self.chatacteristics_table = QTableWidget(self.choose_characteristic_data)
        if (self.chatacteristics_table.columnCount() < 2):
            self.chatacteristics_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.chatacteristics_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.chatacteristics_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.chatacteristics_table.rowCount() < 7):
            self.chatacteristics_table.setRowCount(7)
        self.chatacteristics_table.setObjectName(u"chatacteristics_table")
        self.chatacteristics_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.chatacteristics_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.chatacteristics_table.setRowCount(7)
        self.chatacteristics_table.setColumnCount(2)
        self.chatacteristics_table.horizontalHeader().setMinimumSectionSize(60)
        self.chatacteristics_table.horizontalHeader().setDefaultSectionSize(389)
        self.chatacteristics_table.verticalHeader().setVisible(False)
        self.chatacteristics_table.verticalHeader().setMinimumSectionSize(23)
        self.chatacteristics_table.verticalHeader().setDefaultSectionSize(34)
        self.chatacteristics_table.verticalHeader().setHighlightSections(False)

        self.verticalLayout_2.addWidget(self.chatacteristics_table)

        self.stackedWidget.addWidget(self.parameters_repair)
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(0, 0, 800, 80))
        self.header.setStyleSheet(u"QWidget{\n"
"	background-color: #f1d275;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgba(255, 255, 255, 0.3);\n"
"	border: nune;\n"
"	padding: 10%;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: #ff9d16;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #ff9d16;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: white;\n"
"}")
        self.label = QLabel(self.header)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 7, 180, 31))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.label.setFont(font1)
        self.choose_diagnostic_2 = QWidget(self.header)
        self.choose_diagnostic_2.setObjectName(u"choose_diagnostic_2")
        self.choose_diagnostic_2.setGeometry(QRect(0, 40, 800, 40))
        self.horizontalLayout = QHBoxLayout(self.choose_diagnostic_2)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.choose_diagnostic = QPushButton(self.choose_diagnostic_2)
        self.choose_diagnostic.setObjectName(u"choose_diagnostic")
        font2 = QFont()
        font2.setPointSize(11)
        self.choose_diagnostic.setFont(font2)
        self.choose_diagnostic.setCheckable(True)
        self.choose_diagnostic.setChecked(True)
        self.choose_diagnostic.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.choose_diagnostic)

        self.choose_parrameters = QPushButton(self.choose_diagnostic_2)
        self.choose_parrameters.setObjectName(u"choose_parrameters")
        self.choose_parrameters.setFont(font2)
        self.choose_parrameters.setCheckable(True)
        self.choose_parrameters.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.choose_parrameters)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.choose_diagnostc_list.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u0434\u0438\u0430\u0433\u043d\u043e\u0437", None))
        self.choose_repair_plan_list.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u0441\u043f\u043e\u0441\u043e\u0431 \u0440\u0435\u043c\u043e\u043d\u0442\u0430", None))
        self.repair_plan_update.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u043f\u043e\u0441\u043e\u0431\u044b \u0440\u0435\u043c\u043e\u043d\u0442\u0430", None))
        self.action_tablice_update.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0442\u0430\u0431\u043b\u0438\u0446\u0443", None))
        self.find_diagnostic_button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438 \u0434\u0438\u0430\u0433\u043d\u043e\u0437", None))
        self.find_repairs_button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438 \u0441\u043f\u043e\u0441\u043e\u0431\u044b \u0440\u0435\u043c\u043e\u043d\u0442\u0430", None))
        self.go_to_repair.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u043c\u043e\u043d\u0442", None))
        self.choose_diagnostc_par_list.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u0434\u0438\u0430\u0433\u043d\u043e\u0437", None))
        self.choose_repair_plan_par_list.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u0441\u043f\u043e\u0441\u043e\u0431 \u0440\u0435\u043c\u043e\u043d\u0442\u0430", None))
        ___qtablewidgetitem = self.chatacteristics_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0425\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438", None));
        ___qtablewidgetitem1 = self.chatacteristics_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u044f", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u043c\u043e\u043d\u0442 \u0433\u0438\u0442\u0430\u0440", None))
        self.choose_diagnostic.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0434\u0438\u0430\u0433\u043d\u043e\u0441\u0442\u0438\u043a\u0443", None))
        self.choose_parrameters.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0442\u044c \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
    # retranslateUi

