from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        
        # Configurando o layout basico
        self.cw = QWidget()
        self.vlayout = QVBoxLayout()
        self.cw.setLayout(self.vlayout)
        self.setCentralWidget(self.cw)
        
        # Titulo da janela
        self.setWindowTitle('Calculadora')
        
    def adjustFixedSize(self):
        # Ultima coisa a fazer 
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())