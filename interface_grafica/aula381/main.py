from PySide6.QtWidgets import QWidget, QApplication
from ui_workrui import Ui_myWidget
import sys
import time

class MyWidget(QWidget, Ui_myWidget):
    def __init__(self, parent= None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        
        self.Button1.clicked.connect(self.hardWork1)
        self.Button2.clicked.connect(self.hardWork2)
        
    def hardWork1(self):
        for i in range(5):
            print(i)
            time.sleep(1)
            self.label1.setText('hardWork1 terminado')
        
    def hardWork2(self):
        for i in range(5):
            print(i)
            time.sleep(1)
        self.label2.setText('hardWork2 terminado')
        
if __name__ == '__main__':
    app= QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    app.exec()
    