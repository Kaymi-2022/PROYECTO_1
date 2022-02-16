import sys
from PyQt6.QtWidgets import QMainWindow,QApplication,QTableWidgetItem
from PyQt6.QtGui import * 
from PyQt6 import uic,QtWidgets
import funciones as opera


class Ejemplo01(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("formulario.ui",self)
        self.initUi()
    
    def initUi(self):
        nombreColumnas=("CLIENTE","CANTIDAD","PRECIO","TOTAL", "IGV","PAGO TOTAL")
        self.twgdata.setColumnWidth(0,350)
        self.twgdata.setColumnWidth(1,150)
        self.twgdata.setColumnWidth(2,150)
        self.twgdata.setColumnWidth(3,150)
        self.twgdata.setColumnWidth(4,150)
        self.twgdata.setColumnWidth(5,150)
        self.twgdata.setHorizontalHeaderLabels(nombreColumnas)
        self.b_nuevo.clicked.connect(self.reset)
        self.bagregar.clicked.connect(self.agregar)
        self.bsalir.clicked.connect(self.salir)
        self.cbox_cantidad.activated.connect(self.calcular)
        
        for i in range(100):
            self.cbox_cantidad.addItem(str(i+1))
    
    def reset(self):
        self.txt_cliente.setText("")
        self.lb_precio.setText("")
        self.lb_total.setText("")
        self.lb_igv.setText("")
        self.lb_pagoTotal.setText("")
        self.cbox_cantidad.setCurrentIndex(0)

    def calcular(self):
        cantidad=int(self.cbox_cantidad.itemText(self.cbox_cantidad.currentIndex()))
        self.lb_precio.setText(str(opera.Precio(cantidad)))
        self.lb_total.setText(str(opera.calcularTotal(cantidad)))
        self.lb_igv.setText(str(opera.igv(cantidad)))
        self.lb_pagoTotal.setText(str(opera.pagoTotal(cantidad)))

    def agregar(self):
        nombre=self.txt_cliente.text()
        cantidad=int(self.cbox_cantidad.itemText(self.cbox_cantidad.currentIndex()))
        vprecio=float(self.lb_precio.text())
        vtotal=float(self.lb_total.text())
        vigv=float(self.lb_igv.text())
        vpagoTotal=float(self.lb_pagoTotal.text())
        opera.IngresoDatos(nombre.upper(), cantidad, vprecio, vtotal, vigv, vpagoTotal)
        data=[{"CLIENTE":opera.listado[0],"CANTIDAD":opera.listado[1],
            "PRECIO":opera.listado[2],"TOTAL":opera.listado[3],
            "IGV":opera.listado[4],"PAGO TOTAL":opera.listado[5]}]
        indicefila=self.twgdata.rowCount()
        self.twgdata.insertRow(indicefila)
        
        for dato in data:
            self.twgdata.setItem(indicefila,0,QtWidgets.QTableWidgetItem(dato["CLIENTE"]))
            self.twgdata.setItem(indicefila,1,QtWidgets.QTableWidgetItem(str(dato["CANTIDAD"])))
            self.twgdata.setItem(indicefila,2,QtWidgets.QTableWidgetItem(str(dato["PRECIO"])))
            self.twgdata.setItem(indicefila,3,QtWidgets.QTableWidgetItem(str(dato["TOTAL"])))
            self.twgdata.setItem(indicefila,4,QtWidgets.QTableWidgetItem(str(dato["IGV"])))
            self.twgdata.setItem(indicefila,5,QtWidgets.QTableWidgetItem(str(dato["PAGO TOTAL"])))
            indicefila+=1
        opera.listado.clear()
    
    def salir(self):
        self.close()
            
    


if __name__=='__main__':
    app = QApplication(sys.argv)
    ventana1=Ejemplo01()
    ventana1.show()
    sys.exit(app.exec())
