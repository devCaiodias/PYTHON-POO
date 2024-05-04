from PySide6.QtWidgets import QWidget, QApplication
from ui_workrui import Ui_myWidget
from PySide6.QtCore import QObject, Signal, Slot
import sys
import time

class Worker1(QObject):
    started = Signal(str)
    progressd = Signal(str)
    finished = Signal(str)
    
    def run(self):
        value = '0'
        self.started.emit(value)
        for i in range(5):
            value = str(i)
            self.progressd.emit(value)
            time.sleep(1)
        self.finished.emit(value)

class MyWidget(QWidget, Ui_myWidget):
    def __init__(self, parent= None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        
        self.Button1.clicked.connect(self.hardWork1)
        self.Button2.clicked.connect(self.hardWork2)
        
    @Slot()
    def hardWork1(self):
        self.label1.setText('hardWork1 terminado')
        
    @Slot()
    def hardWork2(self):
        self.label2.setText('hardWork2 terminado')
        
if __name__ == '__main__':
    app= QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    app.exec()
    