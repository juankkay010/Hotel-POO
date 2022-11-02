import sys

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator, QStandardItemModel, QStandardItem
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
        self.dialogo_servicio_turismo = DialogoServicioTurismo()
        self.dialogo_alquiler_vehiculo = DialogoAlquilerVehiculos()
        self.dialogo_salon_belleza = DialogoSalonDeBelleza()
        self.dialogo_lavanderia = DialogoLavanderia()
        self.dialogo_check_out = DialogoCheckOut()
        self.dialogo_limpieza_cuarto = DialogoLimpiezaCuarto()
        self.dialogo_sugerencia = Sugerencias()
        self.hotel = Hotel()
        self.__configurar()

    def __configurar(self):
        # Enlazar eventos de los botones
        self.pb_realizar_reserva.clicked.connect(self.abrir_dialogo_realizar_reserva)
        self.pb_registrar_usuario.clicked.connect(self.abrir_dialogo_registrar_usuario)
        self.pb_cancelar_reserva.clicked.connect(self.abrir_dialogo_cancelar_reserva)
        self.pb_reservar_restaurante.clicked.connect(self.abrir_dialogo_reservar_restaurante)
        self.pb_reservar_zona_entretenimiento.clicked.connect(self.abrir_dialogo_reservar_zona_entretenimiento)
        self.pb_servicio_turismo.clicked.connect(self.abrir_dialogo_servicio_turismo)
        self.pb_alquiler_vehiculo.clicked.connect(self.abrir_dialogo_alquiler_vehiculo)
        self.pb_salon_belleza.clicked.connect(self.abrir_dialogo_salon_belleza)
        self.pb_servicio_lavanderia.clicked.connect(self.abrir_dialogo_lavanderia)
        self.pb_servicio_check_out.clicked.connect(self.abrir_dialogo_check_out)
        self.pb_limpieza_de_cuarto.clicked.connect(self.abrir_dialogo_limpieza_cuarto)
        self.pb_sugerencias.clicked.connect(self.abrir_dialogo_sugerencias)

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

    def abrir_dialogo_servicio_turismo(self):
        resp = self.dialogo_servicio_turismo.exec_()
        if resp == QDialog.Accepted:
            cedula = self.dialogo_servicio_turismo.le_cedula.text()
            hora_reserva = self.dialogo_servicio_turismo.le_hora_reserva.text()
            cantidad_personas = int(self.dialogo_servicio_turismo.le_cantidad_personas.text())
            datos_bancarios = self.dialogo_servicio_turismo.le_datos_bancarios.text()
            lugar_turismo = self.dialogo_servicio_turismo.le_lugar_turismo.text()
            try:
                self.hotel.reserva_servicio_turismo(cedula, hora_reserva, cantidad_personas, datos_bancarios, lugar_turismo)
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Reserva exitosa")
                msg_box.setText(
                    f"Se ha reservado el servicio de turismo {lugar_turismo} a las {hora_reserva} exitosamente")
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
        self.dialogo_servicio_turismo.limpiar()

    def abrir_dialogo_alquiler_vehiculo(self):
        resp = self.dialogo_alquiler_vehiculo.exec_()
        if resp == QDialog.Accepted:
            cedula = self.dialogo_alquiler_vehiculo.le_cedula.text()
            hora_reserva = self.dialogo_alquiler_vehiculo.le_hora_reserva.text()
            cantidad_personas = self.dialogo_alquiler_vehiculo.le_cantidad_personas.text()
            datos_bancarios = self.dialogo_alquiler_vehiculo.le_datos_bancarios.text()
            tipo_vehiculo = self.dialogo_alquiler_vehiculo.le_tipo_vehiculo.text()
            try:
                self.hotel.reserva_vehiculo(cedula, hora_reserva, cantidad_personas, datos_bancarios, tipo_vehiculo)
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Reserva exitosa")
                msg_box.setText(
                    f"Se ha reservado el vehículo {tipo_vehiculo} a las {hora_reserva} exitosamente")
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
        self.dialogo_alquiler_vehiculo.limpiar()

    def abrir_dialogo_salon_belleza(self):
        resp = self.dialogo_salon_belleza.exec_()
        if resp == QDialog.Accepted:
            cedula = self.dialogo_salon_belleza.le_cedula.text()
            hora_reserva = self.dialogo_salon_belleza.le_hora_reserva.text()
            cantidad_personas = self.dialogo_salon_belleza.le_cantidad_personas.text()
            datos_bancarios = self.dialogo_salon_belleza.le_datos_bancarios.text()
            try:
                self.hotel.reserva_servicio_salon_belleza(cedula, hora_reserva, cantidad_personas, datos_bancarios)
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Reserva exitosa")
                msg_box.setText(
                    f"Se ha he reservado la cita a las {hora_reserva} exitosamente")
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
        self.dialogo_salon_belleza.limpiar()

    def abrir_dialogo_lavanderia(self):
        resp = self.dialogo_lavanderia.exec_()
        if resp == QDialog.Accepted:
            cedula = self.dialogo_lavanderia.le_cedula.text()
            hora_reserva = self.dialogo_lavanderia.le_hora_reserva.text()
            try:
                self.hotel.reserva_servicio_lavanderia(cedula, hora_reserva)
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Reserva exitosa")
                msg_box.setText(
                    f"Se ha he reservado la lavanderia a las {hora_reserva} exitosamente")
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
        self.dialogo_lavanderia.limpiar()

    def abrir_dialogo_check_out(self):
        resp = self.dialogo_check_out.exec_()
        if resp == QDialog.Accepted:
            cedula = self.dialogo_check_out.le_cedula.text()
            try:
                self.hotel.servicio_check_out(cedula)
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Reserva finalizada")
                msg_box.setText(
                    f"Se ha finalizado su estadía con exito, esperamos que vuelva pronto. Suerte")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            except ObjetoNoEncontrado as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error")
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setText(err.mensaje)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
        self.dialogo_check_out.limpiar()

    def abrir_dialogo_limpieza_cuarto(self):
        resp = self.dialogo_limpieza_cuarto.exec_()
        if resp == QDialog.Accepted:
            cedula = self.dialogo_limpieza_cuarto.le_cedula.text()
            hora_reserva = self.dialogo_limpieza_cuarto.le_hora_reserva.text()
            try:
                self.hotel.servicio_limpieza_cuarto(cedula, hora_reserva)
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Reserva exitosa")
                msg_box.setText(
                    f"Se ha agendado una limpieza al cuarto a las {hora_reserva} exitosamente")
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
        self.dialogo_limpieza_cuarto.limpiar()

    def abrir_dialogo_sugerencias(self):
        resp = self.dialogo_sugerencia.exec_()
        if resp == QDialog.Accepted:
            mensaje = self.dialogo_sugerencia.le_sugerencia.text()
            self.hotel.escribir_sugerencias(mensaje)
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Sugerencia exitosa")
            msg_box.setText(
                f"Gracias por escribir tu sugerencia, la tendremos en cuenta para mejorar")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()
        self.dialogo_sugerencia.limpiar()


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
        uic.loadUi("gui/DialogoReservarRestaurante.ui", self)
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
        uic.loadUi("gui/DialogoReservarZonaEntretenimiento.ui", self)
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


class DialogoServicioTurismo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("gui/DialogoServicioTurismo.ui", self)
        self.setFixedSize(self.size())

    def limpiar(self):
        self.le_cedula.clear()
        self.le_hora_reserva.clear()
        self.le_cantidad_personas.clear()
        self.le_datos_bancarios.clear()
        self.le_lugar_turismo.clear()

    def accept(self) -> None:
        if self.le_cedula.text() != "" and self.le_hora_reserva.text() != "" and self.le_cantidad_personas != "" and\
                self.le_datos_bancarios.text() != "":
            super(DialogoServicioTurismo, self).accept()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe ingresar todos los campos")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()


class DialogoAlquilerVehiculos(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("gui/DialogoAlquilerVehiculo.ui", self)
        self.setFixedSize(self.size())

    def limpiar(self):
        self.le_cedula.clear()
        self.le_hora_reserva.clear()
        self.le_cantidad_personas.clear()
        self.le_datos_bancarios.clear()
        self.le_tipo_vehiculo.clear()

    def accept(self) -> None:
        if self.le_cedula.text() != "" and self.le_hora_reserva.text() != "" and self.le_cantidad_personas != "" and\
                self.le_datos_bancarios.text() != "" and self.le_tipo_vehiculo.text() != "":
            super(DialogoAlquilerVehiculos, self).accept()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe ingresar todos los campos")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()


class DialogoSalonDeBelleza(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("gui/DialogoSalonDeBelleza.ui", self)
        self.setFixedSize(self.size())

    def limpiar(self):
        self.le_cedula.clear()
        self.le_hora_reserva.clear()
        self.le_cantidad_personas.clear()
        self.le_datos_bancarios.clear()

    def accept(self) -> None:
        if self.le_cedula.text() != "" and self.le_hora_reserva.text() != "" and self.le_cantidad_personas != "" and\
                self.le_datos_bancarios.text() != "":
            super(DialogoSalonDeBelleza, self).accept()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe ingresar todos los campos")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()


class DialogoLavanderia(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("gui/DialogoLavanderia.ui", self)
        self.setFixedSize(self.size())

    def limpiar(self):
        self.le_cedula.clear()
        self.le_hora_reserva.clear()

    def accept(self) -> None:
        if self.le_cedula.text() != "" and self.le_hora_reserva != "":
            super(DialogoLavanderia, self).accept()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe ingresar todos los campos")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()


class DialogoCheckOut(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("gui/DialogoCheckOut.ui", self)
        self.setFixedSize(self.size())

    def limpiar(self):
        self.le_cedula.clear()

    def accept(self) -> None:
        if self.le_cedula.text() != "":
            super(DialogoCheckOut, self).accept()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe ingresar todos los campos")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()


class DialogoLimpiezaCuarto(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("gui/DialogoLimpiezaCuarto.ui", self)
        self.setFixedSize(self.size())

    def limpiar(self):
        self.le_cedula.clear()
        self.le_hora_reserva.clear()

    def accept(self) -> None:
        if self.le_cedula.text() != "" and self.le_hora_reserva != "":
            super(DialogoLimpiezaCuarto, self).accept()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe ingresar todos los campos")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()


class Sugerencias(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("gui/DialogoSugerencias.ui", self)
        self.setFixedSize(self.size())

    def limpiar(self):
        self.le_sugerencia.clear()

    def accept(self) -> None:
        if self.le_sugerencia.text() != "":
            super(Sugerencias, self).accept()
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
