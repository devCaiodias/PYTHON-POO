import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon, QKeyEvent
from variables import WINDOW_ICON_PATH
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QLineEdit
from variables import BIG_FONT_SIZE, MEDIUM_FONT_SIZE, MiNINUM_WIDTH
from buttons import ButtonsGrid
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMessageBox
from util import isEmpty, isNumOrDot

# # Cria aplicação
class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        
        
        # Configurando o layout basico
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)
        
        # Titulo da janela
        self.setWindowTitle('Calculadora')
        
    def adjustFixedSize(self):
        # Ultima coisa a fazer 
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
    
    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)
        
    def mekeMsgBox(self):
        return QMessageBox(self)
     
        
# Infor
class Infor(QLabel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.configStyle()
        
    def configStyle(self):
        self.setAlignment(Qt.AlignmentFlag.AlignRight)     



# Display
class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
        
    def configStyle(self):
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MEDIUM_FONT_SIZE)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key
        
        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete, KEYS.Key_D]
        isEsc = key in [KEYS.Key_Escape, KEYS.Key_C]  
          
        if isEnter or text == '=':
            print(f'Enter {text} pressionado. sinal emitido', type(self).__name__)
            self.eqPressed.emit()
            return event.ignore()
        
        if isDelete:
            print(f'Delete {text} pressionado. sinal emitido', type(self).__name__)
            self.delPressed.emit()
            return event.ignore()
        
        if isEsc:
            print(f'Esc {text} pressionado. sinal emitido', type(self).__name__)
            self.clearPressed.emit()
            return event.ignore()
        
        # N passar daqui se n tiver Texto
        if isEmpty(text):
            return event.ignore()
        
        if isNumOrDot(text):
            print(f'inputPressed {text} pressionado. sinal emitido', type(self).__name__)
            self.inputPressed.emit(text)
            return event.ignore()
            

if __name__ == '__main__':
    # snake_case
    # PascalCase
    # camelCase
    
    # Cria aplicação
    app = QApplication(sys.argv)
    window = MainWindow()
    
    # Definir o Icone
    icon = QIcon(str(WINDOW_ICON_PATH)) # type: ignore
    window.setWindowIcon(icon)
    
    # Infor
    infor = Infor('Sua conta') # type: ignore
    window.addWidgetToVLayout(infor)
    
    # Display
    display = Display()
    display.setPlaceholderText('Number')
    window.addWidgetToVLayout(display)
    
    # Grid
    buttonGrid = ButtonsGrid(display, infor, window)
    window.vLayout.addLayout(buttonGrid)
    
    
    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()