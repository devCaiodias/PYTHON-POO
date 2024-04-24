import sys
from PySide6.QtWidgets import QApplication
from display import Display
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH
from info import Infor

from main_window import MainWindow

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
    infor = Infor('2.0 ^ 10.0 = 1024') # type: ignore
    window.addWidgetToVLayout(infor)
    
    # Display
    display = Display()
    display.setPlaceholderText('Number')
    window.addWidgetToVLayout(display)
    
    
    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()