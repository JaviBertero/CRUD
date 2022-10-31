from email import header
import os,sys
from json import loads
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
#Borrar este mensaje" 
a = open("EFI/data.json")
s = a.read()

data = loads(s)

categorias = ["Nombre","Pais","Mail","Curso","Telefono"]

class BuscarWindow(QWidget):
    def __init__(self):
        super().__init__()
        buscarLayout = self.buscarLayout = QVBoxLayout()

        #Texto
        self.header = header = QLabel("Ingrese características a buscar:")
        buscarLayout.addWidget(header)
        
        #Inputs
        self.input = input = QLineEdit()
        buscarLayout.addWidget(input)
        
        #Botones
        self.botonera = botonera = QHBoxLayout()

        self.botonAceptar = botonAceptar = QPushButton("Aceptar")
        self.botonCancelar = botonCancelar = QPushButton("Cancelar")
        
        botonera.addWidget(botonAceptar)
        botonera.addWidget(botonCancelar)
        
        buscarLayout.addLayout(botonera)

        #Boton Clicker
        botonAceptar.clicked.connect(self.aceptar)
        botonCancelar.clicked.connect(self.cancelar)

        self.setLayout(buscarLayout)
    
    def aceptar(self):
        self.header.setVisible(False)
        self.input.setVisible(False)
        self.botonAceptar.setVisible(False)
        self.botonCancelar.setVisible(False)
        self.buscados = []
        for dic in data:
            for value in dic.values():
                if value.upper() == self.input.text().upper():
                    self.buscados.append(dic)
        
        if len(self.buscados) > 0:
            headerLayout = QHBoxLayout()
            for categoria in categorias:
                cat = QLabel(categoria)
                cat.setAlignment(Qt.AlignCenter)
                headerLayout.addWidget(cat)
            self.buscarLayout.addLayout(headerLayout)

            for dic in self.buscados:
                dato = QHBoxLayout()
                for key,value in dic.items():
                    for categoria in categorias:
                        if key.upper() == categoria.upper():
                            cat = QLabel(value)
                            cat.setAlignment(Qt.AlignCenter)
                            dato.addWidget(cat)
                self.buscarLayout.addLayout(dato)
        else:
            falla = QLabel("No se encontraron coincidencias.")
            headerLayout = QHBoxLayout()
            headerLayout.addWidget(falla)
            self.buscarLayout.addLayout(headerLayout)

        botonera = QHBoxLayout()
        botonSalir = QPushButton("Salir")
        botonera.addWidget(botonSalir)
        botonSalir.clicked.connect(self.cancelar)
        self.buscarLayout.addLayout(botonera)
        
        

    def cancelar(self):
        self.close()

class AgregarWindow(QWidget):
    def __init__(self):
        super().__init__()
        layoutAgregar = QVBoxLayout()

        
        #Texto2
        bodyHeader = QLabel("Ingrese datos:")
        layoutAgregar.addWidget(bodyHeader)

        #Form
        form = QFormLayout()
        layoutAgregar.addLayout(form)

        nombre = QLineEdit()
        pais = QLineEdit()
        mail = QLineEdit()
        curso = QLineEdit()
        telefono = QLineEdit()

        form.addRow("Nombre",nombre)
        form.addRow("Pais",pais)
        form.addRow("Mail",mail)
        form.addRow("Curso",curso)
        form.addRow("Telefono",telefono)
   
        #Botonera
        botonera = QHBoxLayout()
        layoutAgregar.addLayout(botonera)
        
        #Botones
        
        botonConfirmar = QPushButton("Confirmar")
        botonCancelar = QPushButton("Cancelar")

        botonConfirmar.clicked.connect(self.confirmar)
        botonCancelar.clicked.connect(self.cancelar)

        
        botonera.addWidget(botonConfirmar)
        botonera.addWidget(botonCancelar)
    
        self.setLayout(layoutAgregar)
    
    def confirmar(self):
        #Agregar a la base de datos
        print("Se agregó correctamente a la base de datos.")
        self.close()
    
    def cancelar(self):
        self.close()

class EditarWindow(QWidget):
    def __init__(self):
        super().__init__()

        layoutEditar = QVBoxLayout()

        #Texto
        header = QLabel("Ingrese texto a buscar:")
        layoutEditar.addWidget(header)

        #Input
        palabra = QLineEdit()
        layoutEditar.addWidget(palabra)
        
        
        #Botonera
        botonera = QHBoxLayout()
        layoutEditar.addLayout(botonera)

        #Botones
        botonConfirmar = QPushButton("Confirmar")
        botonCancelar = QPushButton("Cancelar")
        
        botonera.addWidget(botonConfirmar)
        botonera.addWidget(botonCancelar)

        self.setLayout(layoutEditar)
    
class EliminarWindow(QWidget):
    def __init__(self):
        super().__init__()

        layoutEliminar = QVBoxLayout()

        self.w1 = BuscarWindow()
        self.w1.show()

        self.setLayout(layoutEliminar)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        mainLayout = QVBoxLayout()

        #Categorias
        headerLayout = QHBoxLayout()
        

        catId  = QLabel("Id")
        catId.setAlignment(Qt.AlignCenter)
        headerLayout.addWidget(catId)

        for categoria in categorias:
            cat = QLabel(categoria)
            cat.setAlignment(Qt.AlignCenter)
            headerLayout.addWidget(cat)

        mainLayout.addLayout(headerLayout)

        #Datos
        dataLayout = QVBoxLayout()
        scroll = QScrollArea()
        widget = QWidget()
        datos1Layout = QVBoxLayout()

        n = 1
        for dic in data:
            id = QLabel(str(n))
            id.setAlignment(Qt.AlignCenter)
            dato = QHBoxLayout()
            dato.addWidget(id)
            n += 1
            for key,value in dic.items():
                for categoria in categorias:
                    if key.upper() == categoria.upper():
                        cat = QLabel(value)
                        cat.setAlignment(Qt.AlignCenter)
                        dato.addWidget(cat)
            datos1Layout.addLayout(dato)

        widget.setLayout(datos1Layout)

        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        scroll.setWidget(widget)

        dataLayout.addWidget(scroll)
        mainLayout.addLayout(dataLayout)
        
        #Botoneras
        botonera1 = QHBoxLayout()
        botonera2 = QHBoxLayout()

        #Botones
        botonBuscar = QPushButton("Buscar")
        botonAgregarItem = QPushButton("Agregar")
        botonEliminarItem = QPushButton("Eliminar")
        botonEditarItem = QPushButton("Editar")
        botonImportarExportar = QPushButton("Importar/Exportar")
        botonSalir = QPushButton("Salir")

        botonBuscar.clicked.connect(self.buscar)
        botonAgregarItem.clicked.connect(self.agregar)
        botonEditarItem.clicked.connect(self.editar)
        botonEliminarItem.clicked.connect(self.eliminar)
        botonSalir.clicked.connect(self.salir)

        botonera1.addWidget(botonBuscar)
        botonera1.addWidget(botonAgregarItem)
        botonera1.addWidget(botonEliminarItem)
        botonera2.addWidget(botonEditarItem)
        botonera2.addWidget(botonImportarExportar)
        botonera2.addWidget(botonSalir)

        mainLayout.addLayout(botonera1)
        mainLayout.addLayout(botonera2)

        centralWidget = QWidget()
        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)
        self.setWindowTitle("Compu Mundo Hiper Mega Red")

    def buscar(self):
        self.w = BuscarWindow()
        self.w.show()
    
    def agregar(self):
        self.w = AgregarWindow()
        self.w.show()

    def editar(self):
        self.w = EditarWindow()
        self.w.show()
    
    def eliminar(self):
        self.w = EliminarWindow()
        self.w.show()
    
    def salir(self):
        ventana.close()

if __name__ == "__main__":
    
    aplicacion = QApplication()
    ventana = MainWindow()
    ventana.show()
    aplicacion.exec()