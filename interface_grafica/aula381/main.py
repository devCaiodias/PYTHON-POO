from PySide6.QtWidgets import QWidget, QApplication
from ui_workrui import Ui_myWidget
from PySide6.QtCore import QObject, Signal, Slot, QThread
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
        self._worker = Worker1()
        self._thread = QThread()
        
        worker = self._worker
        thread = self._thread
        
        # Movero o Worker para a theread
        worker.moveToThread(thread)
        
        # Run
        thread.started.connect(worker.run)
        worker.finished.connect(thread.quit)
        
        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)
        
        worker.started.connect(self.workerStart)
        worker.progressd.connect(self.inProgressd)
        worker.finished.connect(self.workerFinishe)
        
        thread.start()
        
    def workerStart(self, value):
        self.Button1.setDisabled(True)
        self.label1.setText(value)
        print('Go worker!')
        
    def inProgressd(self, value):
        self.label1.setText(value)
        print('in progressd')
        
    def workerFinishe(self, value):
        self.Button1.setDisabled(False)
        self.label1.setText(value)
        print('Finishe worker!')
        
    @Slot()
    def hardWork2(self):
        self._worker2 = Worker1()
        self._thread2 = QThread()
        
        worker = self._worker2
        thread = self._thread2
        
        # Movero o Worker para a theread
        worker.moveToThread(thread)
        
        # Run
        thread.started.connect(worker.run)
        worker.finished.connect(thread.quit)
        
        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)
        
        worker.started.connect(self.worker2Start)
        worker.progressd.connect(self.inProgressd2)
        worker.finished.connect(self.worker2Finishe)
        
        thread.start()
        
    def worker2Start(self, value):
        self.Button2.setDisabled(True)
        self.label2.setText(value)
        print('Go 2 worker!')
        
    def inProgressd2(self, value):
        self.label2.setText(value)
        print('in 2 progressd')
        
    def worker2Finishe(self, value):
        self.Button2.setDisabled(False)
        self.label2.setText(value)
        print('Finishe 2 worker!')
        
if __name__ == '__main__':
    app= QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    app.exec()
    