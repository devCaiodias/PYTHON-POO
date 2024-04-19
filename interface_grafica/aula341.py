# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6

import sys
from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

botao = QPushButton('BUTTON')
botao.setStyleSheet('font-size: 40px; color: red')
botao.show() # Adicionar o widget na hierarquia e exibe a Janela


app.exec() # Executa o lup da aplicação