import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from controler import buscarRes, buscarContenido

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("scrapping.ui", self)
        self.setWindowTitle("Web Scrapping")
        self.resultTable.setColumnWidth(0,600)
        self.resultTable.setColumnWidth(1,180)
        self.resultTable.setColumnWidth(2,250)
        self.barraProgreso.setVisible(False)
        self.buscarBoton.clicked.connect(self.loaddata)
        self.contenido_completo = None

    def loaddata(self):
        self.barraProgreso.setVisible(True)
        self.barraProgreso.setValue(0)
        if self.contenido_completo == None:
            self.contenido_completo = buscarContenido(self.barraProgreso)

        productos = buscarRes(self.palabraClave.text().upper(), self.contenido_completo, self.barraProgreso)
        self.resultTable.setRowCount(len(productos))
        row = 0
        for producto in productos:
            self.resultTable.setItem(row, 0, QtWidgets.QTableWidgetItem(producto["nombre"]))
            self.resultTable.setItem(row, 1, QtWidgets.QTableWidgetItem(producto["precio"]))
            self.resultTable.setItem(row, 2, QtWidgets.QTableWidgetItem(producto["tienda"]))
            row += 1
        self.barraProgreso.setValue(100)
        self.barraProgreso.setVisible(False)
app = QApplication(sys.argv)
window = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.setWindowTitle("Web Scrapping")
widget.addWidget(window)
widget.setFixedWidth(1240)
widget.setFixedHeight(580)
widget.show()
try: 
    sys.exit(app.exec_())
except:
    print("Exiting")