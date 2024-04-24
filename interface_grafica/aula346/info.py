from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtCore import Qt

class Infor(QLabel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.configStyle()
        
    def configStyle(self):
        self.setAlignment(Qt.AlignmentFlag.AlignRight)