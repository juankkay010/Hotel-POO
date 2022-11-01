import sys

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox
from PyQt5 import uic

from hotel.mundo.excepciones import ObjetoExistente, ObjetoNoEncontrado
from hotel.mundo.hotel import Hotel


class MainWindowHotel(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("gui/MainWindowHotel.ui", self)
        self.setFixedSize(self.size())
        self.dialogo_realizar_reserva = DialogoRealizarReserva()
        self.dialogo_registrar_usuario = DialogoRegistrarUsuario()
        self.dialogo_cancelar_reserva = DialogoCancelarReserva()
        self.dialogo_reservar_restaurante = DialogoReservarRestaurante()
        self.dialogo_reservar_zona_entretenimiento = DialogoReservarZonaEntretenimiento()
        self.hotel = Hotel()
        self.__configurar()

    def __configurar(self):
        # Enlazar eventos de los botones
        self.pb_realizar_reserva.clicked.connect(self.abrir_dialogo_realizar_reserva)
        self.pb_registrar_usuario.clicked.connect(self.abrir_dialogo_registrar_usuario)
        self.pb_cancelar_reserva.clicked.connect(self.abrir_dialogo_cancelar_reserva)
        self.pb_reservar_restaurante.clicked.connect(self.abrir_dialogo_reservar_restaurante)
        self.pb_reservar_zona_entretenimiento.clicked.connect(self.abrir_dialogo_reservar_zona_entretenimiento)

    def abrir_dialogo_realizar_reserva(self):
        resp = self.dialogo_realizar_reserva.exec_()
        if resp == QDialog.Accepted:
            cedula = self.dialogo_realizar_reserva.le_cedula.text()
            nombre = self.dialogo_realizar_reserva.le_nombre.text()
            cantidad_noches = int(self.dialogo_realizar_reserva.le_cantidad_noches.text())
            cantidad_personas = int(self.dialogo_realizar_reserva.le_cantidad_personas.text())
            try:
                self.hotel.realizar_reserva(cedula, nombre, cantidad_noches, cantidad_personas)
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Reserva exitosa")
                msg_box.setText(f"Se ha hecho la reserva exitosamente, su número de habitación es "
                                f"{self.hotel.numero_habitacion}")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            except ObjetoExistente as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error")
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setText(err.mensaje)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
        self.dialogo_realizar_reserva.limpiar()

    def abrir_dialogo_registrar_usuario(self):
        resp = self.dialogo_registrar_usuario.exec_()
        if resp == QDialog.Accepted:
            cedula = self.dialogo_registrar_usuario.le_cedula.text()
            nombre = self.dialogo_realizar_reserva.le_nombre.text()
            fecha_nacimiento = self.dialogo_registrar_usuario.le_fecha_nacimiento.text()
            numero_habitacion = self.dialogo_registrar_usuario.le_numero_habitacion.text()
            try:
                self.hotel.registrar_usuario(cedula, nombre, fecha_nacimiento, numero_habitacion)
            except ObjetoExistente as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error")
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setText(err.mensaje)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
        self.dialogo_registrar_usuario.limpiar()

    def abrir_dialogo_cancelar_reserva(self):
        resp = self.dialogo_cancelar_reserva.exec_()
        if resp == QDialog.Accepted:
            cedula = self.dialogo_cancelar_reserva.le_cedula.text()
            try:
                self.hotel.cancelar_reserva(cedula)
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Reserva cancelada")
                msg_box.setText(
                    f"Se ha cancelado la reserva exitosamente")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            except ObjetoNoEncontrado as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error")
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setText(err.mensaje)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
        self.dialogo_cancelar_reserva.limpiar()

    def abrir_dialogo_reservar_restaurante(self):
        resp = self.dialogo_reservar_restaurante.exec_()
        if resp == QDialog.Accepted:
            cedula = self.dialogo_reservar_restaurante.le_cedula.text()
            hora_reserva = self.dialogo_reservar_restaurante.le_hora_reserva.text()
            cantidad_personas = int(self.dialogo_reservar_restaurante.le_cantidad_personas.text())
            try:
                self.hotel.reservar_restaurante(cedula, cantidad_personas, hora_reserva)
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Reserva exitosa")
                msg_box.setText(
                    f"Se ha reservado el restaurante a las {hora_reserva} exitosamente")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            except ObjetoExistente as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error")
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setText(err.mensaje)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            except ObjetoNoEncontrado as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error")
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setText(err.mensaje)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
        self.dialogo_reservar_restaurante.limpiar()

    def abrir_dialogo_reservar_zona_entretenimiento(self):
        resp = self.dialogo_reservar_zona_entretenimiento.exec_()
        if resp == QDialog.Accepted:
            cedula = self.dialogo_reservar_zona_entretenimiento.le_cedula.text()
            hora_reserva = self.dialogo_reservar_zona_entretenimiento.le_hora_reserva.text()
            cantidad_personas = int(self.dialogo_reservar_zona_entretenimiento.le_cantidad_personas.text())
            zona_entretenimiento = self.dialogo_reservar_zona_entretenimiento.le_zona_entretenimiento.text()
            try:
                self.hotel.reservar_zona_entretenimiento(cedula, hora_reserva, cantidad_personas, zona_entretenimiento)
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Reserva exitosa")
                msg_box.setText(
                    f"Se ha reservado la zona de entretenimiento {zona_entretenimiento} a las {hora_reserva} exitosamente")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            except ObjetoExistente as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error")
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setText(err.mensaje)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            except ObjetoNoEncontrado as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error")
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setText(err.mensaje)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
        self.dialogo_reservar_zona_entretenimiento.limpiar()


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
        if self.le_cedula.text() != "" and self.le_cantidad_noches.text() != "" and self.le_cantidad_personas.text()\
                != "" and self.le_nombre.text() != "":
            super(DialogoRealizarReserva, self).accept()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe ingresar todos los campos")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()


class DialogoRegistrarUsuario(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("gui/DialogoRegistrarUsuario.ui", self)
        self.setFixedSize(self.size())

    def limpiar(self):
        self.le_cedula.clear()
        self.le_nombre.clear()
        self.le_fecha_nacimiento.clear()
        self.le_numero_habitacion.clear()

    def accept(self) -> None:
        if self.le_cedula.text() != "" and self.le_nombre.text() != "" and self.le_fecha_nacimiento.text() != "" \
                and self.le_numero_habitacion.text() != "":
            super(DialogoRegistrarUsuario, self).accept()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe ingresar todos los campos")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()


class DialogoCancelarReserva(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("gui/CancelarReserva.ui", self)
        self.setFixedSize(self.size())

    def limpiar(self):
        self.le_cedula.clear()

    def accept(self) -> None:
        if self.le_cedula.text() != "":
            super(DialogoCancelarReserva, self).accept()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe ingresar todos los campos")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()


class DialogoReservarRestaurante(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("gui/ReservarRestaurante.ui", self)
        self.setFixedSize(self.size())

    def limpiar(self):
        self.le_cedula.clear()
        self.le_hora_reserva.clear()
        self.le_cantidad_personas.clear()

    def accept(self) -> None:
        if self.le_cedula.text() != "" and self.le_hora_reserva.text() != "" and self.le_cantidad_personas != "":
            super(DialogoReservarRestaurante, self).accept()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe ingresar todos los campos")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()


class DialogoReservarZonaEntretenimiento(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("gui/ReservarZonaEntretenimiento.ui", self)
        self.setFixedSize(self.size())

    def limpiar(self):
        self.le_cedula.clear()
        self.le_hora_reserva.clear()
        self.le_cantidad_personas.clear()
        self.le_zona_entretenimiento.clear()

    def accept(self) -> None:
        if self.le_cedula.text() != "" and self.le_hora_reserva.text() != "" and self.le_cantidad_personas != "" and\
                self.le_zona_entretenimiento != "":
            super(DialogoReservarZonaEntretenimiento, self).accept()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe ingresar todos los campos")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindowHotel()
    win.show()
    sys.exit(app.exec_())
