from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget
from variables import MEDIUM_FONT_SIZE
from util import isEmpty, isNumOrDot, isValidNumber
from PySide6.QtCore import Slot

from typing  import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Display
    from main import Infor

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
        

class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'Infor',  *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['👨‍💻', '0', '.', '=' ],
        ]
        self.display = display
        self.info = info
        self._equation = ''
        self._maskGrid()
        
    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self, valor):
        self._equation = valor
        self.info.setText(valor)
        
    
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
        textButton = button.text()
        newDisplayValue = self.display.text() + textButton
        
        if not isValidNumber(newDisplayValue):
            return
        self.display.insert(textButton)
        
        