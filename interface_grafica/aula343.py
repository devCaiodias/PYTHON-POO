# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec

import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QPushButton, QWidget, QGridLayout, QMainWindow)

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Minha Janela')

botao = QPushButton('BUTTON')
botao.setStyleSheet('font-size: 20px; color: red')
# botao.show() # Adicionar o widget na hierarquia e exibe a Janela

botao2 = QPushButton('BUTTON2')
botao2.setStyleSheet('font-size: 20px; color: red')
# botao2.show()

botao3 = QPushButton('BUTTON3')
botao3.setStyleSheet('font-size: 20px; color: red')

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao, 1 , 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

@Slot()
def slot_exemplo(status_bar):
    status_bar.showMessage('Caio lindooo')
    
@Slot()   
def outro_slot(checked):
    print('está Marcado? ', checked)
    
@Slot()    
def terceiro_slot(action):
    def interna():
        outro_slot(action.isChecked())
    return interna

# StatusBar
status_bar = window.statusBar()

status_bar.showMessage('Mostrando um Menssagem na barra')

# MenuBar
menu_bar = window.menuBar()
primeiro_menu = menu_bar.addMenu('Primeiro menu')
primeiro_acao = primeiro_menu.addAction('Primeira Ação') # type: ignore
primeiro_acao.triggered.connect(lambda: slot_exemplo(status_bar)) # type: ignore


segendo_action = primeiro_menu.addAction('Primeira Ação') # type: ignore
segendo_action.setCheckable(True)
segendo_action.toggled.connect(outro_slot) # type: ignore
segendo_action.hovered.connect(terceiro_slot(segendo_action)) # type: ignore


botao.clicked.connect(terceiro_slot(segendo_action))



window.show()  # Central widget entre na hierarquia e mostra sua janela
app.exec() # Executa o lup da aplicação