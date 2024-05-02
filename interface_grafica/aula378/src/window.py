# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(507, 410)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        font = QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)

        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.LabelName = QLabel(self.centralwidget)
        self.LabelName.setObjectName(u"LabelName")
        self.LabelName.setFont(font)

        self.gridLayout_2.addWidget(self.LabelName, 0, 1, 1, 1)

        self.LineName = QLineEdit(self.centralwidget)
        self.LineName.setObjectName(u"LineName")
        self.LineName.setFont(font)

        self.gridLayout_2.addWidget(self.LineName, 0, 2, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 1, 1, 1)

        self.LabelResult = QLabel(self.centralwidget)
        self.LabelResult.setObjectName(u"LabelResult")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.LabelResult.setFont(font1)
        self.LabelResult.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.LabelResult, 0, 1, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 507, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Ok!", None))
        self.LabelName.setText(QCoreApplication.translate("MainWindow", u"My name:", None))
        self.LineName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Dijite seu nome", None))
        self.LabelResult.setText(QCoreApplication.translate("MainWindow", u"Nada aki", None))
    # retranslateUi

