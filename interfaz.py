import sys

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox
from PyQt5 import uic

from hotel.mundo.excepciones import ReservaExistente
from hotel.mundo.hotel import Hotel


class MainWindowHotel(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("gui/MainWindowHotel.ui", self)
        self.setFixedSize(self.size())
        self.dialogo_realizar_reserva = DialogoRealizarReserva()
        self.hotel = Hotel()
        self.__configurar()

    def __configurar(self):
        # Enlazar eventos de los botones
        self.pb_realizar_reserva.clicked.connect(self.abrir_dialogo_realizar_reserva)

    def abrir_dialogo_realizar_reserva(self):
        resp = self.dialogo_realizar_reserva.exec_()
        if resp == QDialog.Accepted:
            cedula = self.dialogo_realizar_reserva.le_cedula.text()
            nombre = self.dialogo_realizar_reserva.le_nombre.text()
            cantidad_noches = int(self.dialogo_realizar_reserva.le_cantidad_noches.text())
            cantidad_personas = int(self.dialogo_realizar_reserva.le_cantidad_personas.text())
            try:
                self.hotel.realizar_reserva(cedula, nombre, cantidad_noches, cantidad_personas)
            except ReservaExistente as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error")
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setText(err.mensaje)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
        self.dialogo_realizar_reserva.limpiar()


class DialogoRealizarReserva(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("gui/DialogoRealizarReserva.ui", self)
        self.setFixedSize(self.size())

    def __configurar(self):
        self.le_cedula.setValidator(QRegExpValidator(QRegExp("\\d{5}"), self.le_cedula))
        self.le_cantidad_noches.setValidator(QRegExpValidator(QRegExp("\\d{1}"), self.le_cantidad_noches))
        self.le_cantidad_personas.setValidator(QRegExpValidator(QRegExp("\\d{1}"), self.le_cantidad_personas))

    def limpiar(self):
        self.le_cedula.clear()
        self.le_nombre.clear()
        self.le_cantidad_noches.clear()
        self.le_cantidad_personas.clear()

    def accept(self) -> None:
        if self.le_cedula.text() != "" and self.le_cantidad_noches.text() != "" \
                and self.le_cantidad_personas.text() != "" and self.le_nombre.text() != "":
            super(DialogoRealizarReserva, self).accept()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe ingresar todos los campos")
            msg_box.setStandardButtons(QMessageBox.Ok)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindowHotel()
    win.show()
    sys.exit(app.exec_())
