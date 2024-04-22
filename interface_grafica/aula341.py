# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6

import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout

app = QApplication(sys.argv)

botao = QPushButton('BUTTON')
botao.setStyleSheet('font-size: 20px; color: red')
# botao.show() # Adicionar o widget na hierarquia e exibe a Janela

botao2 = QPushButton('BUTTON2')
botao2.setStyleSheet('font-size: 20px; color: red')
# botao2.show()

botao3 = QPushButton('BUTTON3')
botao3.setStyleSheet('font-size: 20px; color: red')

central_widget = QWidget()


layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao, 1 , 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)


central_widget.show()  # Central widget entre na hierarquia e mostra sua janela
app.exec() # Executa o lup da aplicação