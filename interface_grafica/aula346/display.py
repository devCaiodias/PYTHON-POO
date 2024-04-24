from PySide6.QtWidgets import QLineEdit
from variables import BIG_FONT_SIZE, MEDIUM_FONT_SIZE, MiNINUM_WIDTH
from PySide6.QtCore import Qt


class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
        
    def configStyle(self):
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MEDIUM_FONT_SIZE)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        