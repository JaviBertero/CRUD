from json import loads

import sys

a = open("EFI/data.json")
s = a.read()

data = loads(s)

from PySide6.QtCore import Qt, QSize

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QFrame,
    QLabel,
    QFormLayout,
    QScrollArea
)
from PySide6.QtGui import *

categorias = ["Nombre","Pais","Mail","Curso","Telefono"]

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        
        mainLayout = QVBoxLayout()

        input = self.input = QLineEdit()
        mainLayout.addWidget(input)

        botonera = QHBoxLayout()
        mainLayout.addLayout(botonera)
        boton = QPushButton("Buscar")
        botonera.addWidget(boton)
        boton.clicked.connect(self.buscar)

        

        centralWidget = QWidget()
        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)

    def buscar(self):
        for dic in data:
            for value in dic.values():
                if value == self.input.text():
                    print(dic)
        self.close()
        


if __name__ == "__main__":
    
    aplicacion = QApplication()
    ventana = MainWindow()
    ventana.show()
    aplicacion.exec()