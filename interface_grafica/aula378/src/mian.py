from PySide6.QtCore import QEvent, QObject
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QKeyEvent
from window import Ui_MainWindow
from typing import cast
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent= None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.changeLabelResult)
        
        self.LineName.installEventFilter(self)
        
    def changeLabelResult(self):
        text = self.LineName.text()
        self.LabelResult.setText(text)
        
    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.Type.KeyPress: 
            event = cast(QKeyEvent, event)
            print(event.text())
        return super().eventFilter(watched, event)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()