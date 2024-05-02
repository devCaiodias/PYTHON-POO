from PySide6.QtWidgets import QMainWindow, QApplication
from window import Ui_MainWindow
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent= None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.changeLabelResult)
        
    def changeLabelResult(self):
        text = self.LineName.text()
        self.LabelResult.setText(text)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()