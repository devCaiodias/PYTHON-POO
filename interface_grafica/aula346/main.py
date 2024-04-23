import sys
from PySide6.QtWidgets import QApplication, QLineEdit, QTextEdit
from display import Display
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH

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
    
    # Display
    display = Display()
    display.setPlaceholderText('Number')
    window.addWidgetToVLayout(display)
    
    
    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()