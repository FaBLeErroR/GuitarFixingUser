# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_repair.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QDialog,
    QHeaderView, QLabel, QSizePolicy, QTableView,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 500)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 780, 480))
        self.widget.setStyleSheet(u"Line{\n"
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
        self.repair_plan = QLabel(self.widget)
        self.repair_plan.setObjectName(u"repair_plan")
        self.repair_plan.setGeometry(QRect(0, 0, 780, 40))
        font = QFont()
        font.setPointSize(24)
        self.repair_plan.setFont(font)
        self.repair_plan.setAlignment(Qt.AlignCenter)
        self.repair_table_alone = QTableView(self.widget)
        self.repair_table_alone.setObjectName(u"repair_table_alone")
        self.repair_table_alone.setGeometry(QRect(0, 50, 780, 430))
        self.repair_table_alone.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.repair_table_alone.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.repair_table_alone.horizontalHeader().setCascadingSectionResizes(True)
        self.repair_table_alone.verticalHeader().setVisible(False)
        self.repair_table_alone.verticalHeader().setHighlightSections(False)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.repair_plan.setText(QCoreApplication.translate("Dialog", u"\u041f\u043b\u0430\u043d \u0440\u0435\u043c\u043e\u043d\u0442\u0430", None))
    # retranslateUi

