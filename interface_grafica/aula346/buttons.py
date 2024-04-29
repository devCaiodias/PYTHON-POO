from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import MEDIUM_FONT_SIZE
from util import isEmpty, isNumOrDot, isValidNumber
from PySide6.QtCore import Slot
from math import pow

from typing  import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Display
    from main import MainWindow
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
    def __init__(self, display: 'Display', info: 'Infor', window: 'MainWindow',  *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        self._gridMask = [
            ['C', 'D', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['👨‍💻', '0', '.', '=' ],
        ]
        self.display = display
        self.info = info
        self.window = window
        self._equation = ''
        self._equationInitialValue = 'Sua conta'
        self._left = None
        self._right = None
        self._op = None
        
        self.equation = self._equationInitialValue
        self._maskGrid()
        
    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self, valor):
        self._equation = valor
        self.info.setText(valor)
    
    def _vouApagarVc(self, *args, **kwargs):
        print('Sinal pressionado. sinal emitido', type(self).__name__, args, kwargs)    
    
    
    def _maskGrid(self):
        self.display.eqPressed.connect(self._vouApagarVc)
        self.display.delPressed.connect(self.display.backspace)
        self.display.clearPressed.connect(self._clear)
        self.display.inputPressed.connect(self._vouApagarVc)
        self.display.operaitorPressed.connect(self._vouApagarVc)
        
        for rowNumber, row in enumerate(self._gridMask):
            for colunsNumber, button_text in enumerate(row):
                button = Button(button_text)
                
                if not isNumOrDot(button_text) and not isEmpty(button_text):
                    self._connectSpacialButton(button)
                
                
                self.addWidget(button, rowNumber, colunsNumber)
                slotButton = self._makeSlot(self._insertButtonTextToDisplay,button,)
                self._connectButtonClick(button,slotButton) # type: ignore
                
                
    def _connectButtonClick(self, button, slot):
        button.clicked.connect(slot)
    
    def _connectSpacialButton(self, button):
        text = button.text()
        
        if text == 'C':
            self._connectButtonClick(button, self._clear)
            
        if text == 'D':
            self._connectButtonClick(button, self.display.backspace)
            
        if text in '+-/*^':
            self._connectButtonClick(button, self._makeSlot(self._operatoClicked, button))
            
        if text == '=':
            self._connectButtonClick(button, self._eq)
            
        
    def _makeSlot(self, method, *args, **kargs):
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
        
    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
        self.display.clear()
        
    def _operatoClicked(self, button):
        text = button.text() # +-/* (etec...)
        displayText = self.display.text() # Deverá ser meu número _left
        self._clear() # Limpa o display
        
        # Se a pessoa clicou no operador sem configurar qualquer numero
        if not isValidNumber(displayText) and self._left is None:
            self._showError('VOCÊ NÃO DIJITOU NADA.')
            return
            
            
        # Se hover algo no número da esquerda n fazemos nada. Aquardaremos o número da direita
        if self._left is None:
            self._left = float(displayText)
            
        self._op = text
        self.equation = f'{self._left} {self._op} ??'

    def _eq(self):
        displayText = self.display.text()
        
        if not isValidNumber(displayText):
            self._showError('Conta incompleta')
            return
        
        self._right = float(displayText)
        self.equation = f'{self._left} {self._op} {self._right}'
        result = 'error'
        
        try:
            if '^' in self.equation and self._left is not None:
                result = pow(self._left, self._right)
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self._showError('Vc n pode dividir numero por 0')
        except OverflowError:
            self._showError('Essa conta n pode ser realizada')
            
        self.display.clear
        self.info.setText(f'{self.equation} = {result}')
        self.display.setText(str(result)) # type: ignore
        self._right = None
        
        if result == 'error':
            self._left = None
            
    def _makeDialog(self, text):
        msgBox = self.window.mekeMsgBox()
        msgBox.setText(text)
        return msgBox
            
    def _showError(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.exec()
    
    def _showInfo(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.exec()