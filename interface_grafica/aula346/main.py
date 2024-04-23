import sys
from PySide6.QtWidgets import QApplication,QLabel

from main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    
    lable1 = QLabel('Caio no codigo')
    lable1.setStyleSheet('font-size: 150px')
    window.vlayout.addWidget(lable1)
    window.adjustFixedSize()
    
    window.show()
    app.exec()