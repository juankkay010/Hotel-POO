import random
import datetime
from typing import Optional

from hotel.mundo.excepciones import ObjetoExistente, ObjetoNoEncontrado


class Usuario:

    def __init__(self, nombre: str, cedula: str, fecha_nacimiento: datetime, numero_habitacion: str):
        self.nombre = nombre
        self.cedula = cedula
        self.fecha_nacimiento = fecha_nacimiento
        self.numero_habitacion = numero_habitacion

    def __str__(self) -> str:
        return f"{self.cedula} - {self.nombre} - {self.fecha_nacimiento}"


class Checkin:

    def __init__(self, cedula: str, nombre: str, cantidad_noches: int, cantidad_personas: int, numero_habitacion: str):
        self.cedula = cedula
        self.nombre = nombre
        self.cantidad_noches = cantidad_noches
        self.cantidad_personas = cantidad_personas
        self.numero_habitacion = numero_habitacion


class Reserva:

    def __init__(self, cedula: str, cantidad_personas: int, hora_reserva: str):
        self.cedula = cedula
        self.cantidad_personas = cantidad_personas
        self.hora_reserva = hora_reserva


class Servicio:

    def __init__(self, nombre: str, cedula: str, hora_servicio: str, cantidad_personas: int, cantidad_dias: Optional[int], datos_tarjeta_bancaria: Optional[str]):
        self.nombre = nombre
        self.cedula = cedula
        self.hora_servicio = hora_servicio
        self.cantidad_personas = cantidad_personas
        self.cantidad_dias = cantidad_dias
        self.datos_tarjeta_bancaria = datos_tarjeta_bancaria


class Hotel:

    numero_habitacion = str(random.randint(1, 10))

    def __init__(self):
        self.usuario = {}
        self.checkin = {}
        self.restaurante = {}
        self.zonas_entretenimiento = {}
        self.turismo = {}
        self.alquiler = {}
        self.belleza = {}

    def buscar_usuario(self, cedula) -> Optional[Usuario]:
        if cedula in self.usuario.keys():
            return self.usuario[cedula]
        else:
            return None

    def registrar_usuario(self, cedula: str, nombre: str, fecha_nacimiento: datetime, numero_habitacion: str):
        if self.buscar_usuario(cedula) is None:
            usuario = Usuario(cedula, nombre, fecha_nacimiento, numero_habitacion)
            self.usuario[cedula] = usuario
        else:
            raise ObjetoExistente(f"Ya existe un usuario con la cédula {cedula}", cedula)

    def buscar_reserva(self, cedula) -> Optional[Checkin]:
        if cedula in self.checkin.keys():
            return self.checkin[cedula]
        else:
            return None

    def realizar_reserva(self, cedula: str, nombre: str, cantidad_noches: int, cantidad_personas: int):
        if self.buscar_reserva(cedula) is None:
            reserva = Checkin(cedula, nombre, cantidad_noches, cantidad_personas, self.numero_habitacion)
            self.checkin[cedula] = reserva
        else:
            raise ObjetoExistente(f"Ya existe una reserva con la cédula {cedula}", cedula)

    def cancelar_reserva(self, cedula):
        if self.buscar_reserva(cedula) is not None:
            del self.checkin[cedula]
        else:
            raise ObjetoNoEncontrado(f"No existe una reserva con la cédula {cedula}", cedula)

    def buscar_reserva_restaurante(self, cedula) -> Optional[Reserva]:
        if cedula in self.restaurante.keys():
            return self.restaurante[cedula]
        else:
            return None

    def reservar_restaurante(self, cedula: str, hora_reserva: str, cantidad_personas: int):
        if self.buscar_reserva(cedula) is not None:
            if self.buscar_reserva_restaurante(cedula) is None:
                reserva_restaurante = Reserva(cedula, cantidad_personas, hora_reserva)
                self.restaurante[cedula] = reserva_restaurante
            else:
                raise ObjetoExistente(f"Ya existe una reserva con la cédula {cedula}", cedula)
        else:
            raise ObjetoNoEncontrado(f"No existe una reserva con la cédula {cedula}", cedula)
