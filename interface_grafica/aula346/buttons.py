from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget
from variables import MEDIUM_FONT_SIZE
from util import isEmpty, isNumOrDot
from PySide6.QtCore import Slot

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
    
    def configStyle(self):
        # self.setStyleSheet(f'font-size: {MEDIUM_FONT_SIZE}px')
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        # font.setItalic(True)
        font.setBold(True)
        self.setFont(font)
        self.setMinimumSize(45, 45)
        self.setCheckable(True)
        

class ButtonsGrid(QGridLayout):
    def __init__(self, display, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['👨‍💻', '0', '.', '=' ],
        ]
        self.display = display
        self._maskGrid()
        
    
    def _maskGrid(self):
        for rowNumber, row in enumerate(self._gridMask):
            for colunsNumber, button_text in enumerate(row):
                button = Button(button_text)
                
                
                self.addWidget(button, rowNumber, colunsNumber)
                slotButton = self._makeButtonDisplaySlot(
                    self._insertButtonTextToDisplay,
                    button,
                    )
                button.clicked.connect(slotButton) # type: ignore
            
    def _makeButtonDisplaySlot(self, method, *args, **kargs):
        @Slot(bool)
        def realSlot(_):
            method(*args, **kargs)
        return realSlot
    
    def _insertButtonTextToDisplay(self, button):
        text_button = button.text()
        self.display.insert(text_button)