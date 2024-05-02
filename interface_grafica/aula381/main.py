from PySide6.QtWidgets import QWidget, QApplication
from ui_workrui import Ui_myWidget
import sys

class MyWidget(QWidget, Ui_myWidget):
    def __init__(self, parent= None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        
if __name__ == '__main__':
    app= QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    app.exec()
    