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

    def __init__(self, cedula: str, hora_servicio: str, cantidad_personas:  Optional[int], datos_tarjeta_bancaria: Optional[str]):
        self.cedula = cedula
        self.hora_servicio = hora_servicio
        self.cantidad_personas = cantidad_personas
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
        self.lavanderia = {}
        self.limpieza = {}
        self.sugerencias = []

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

    def buscar_reserva_zona_entretenimiento(self, cedula) -> Optional[Reserva]:
        if cedula in self.zonas_entretenimiento.keys():
            return self.zonas_entretenimiento[cedula]
        else:
            return None

    def reservar_zona_entretenimiento(self, cedula: str, hora_reserva: str, cantidad_personas: int, zona_entretenimiento: str):
        if self.buscar_reserva(cedula) is not None:
            if self.buscar_reserva_zona_entretenimiento(cedula) is None:
                reserva_zona_entretenimiento: tuple = (Reserva(cedula, cantidad_personas, hora_reserva), zona_entretenimiento)
                self.zonas_entretenimiento[cedula] = reserva_zona_entretenimiento
            else:
                raise ObjetoExistente(f"Ya existe una reserva con la cédula {cedula}", cedula)
        else:
            raise ObjetoNoEncontrado(f"No existe una reserva con la cédula {cedula}", cedula)

    def buscar_reserva_turismo(self, cedula) -> Optional[Servicio]:
        if cedula in self.turismo.keys():
            return self.turismo[cedula]
        else:
            return None

    def reserva_servicio_turismo(self, cedula: str, hora_reserva: str, cantidad_personas: int, datos_tarjeta_bancaria: Optional[str], lugar_turismo: str):
        if self.buscar_reserva(cedula) is not None:
            if self.buscar_reserva_turismo(cedula) is None:
                reserva_turismo: tuple = (Servicio(cedula, hora_reserva, cantidad_personas, datos_tarjeta_bancaria), lugar_turismo)
                self.turismo[cedula] = reserva_turismo
            else:
                raise ObjetoExistente(f"Ya existe una reserva con la cédula {cedula}", cedula)
        else:
            raise ObjetoNoEncontrado(f"No existe una reserva con la cédula {cedula}", cedula)

    def buscar_alquiler_vehiculo(self, cedula) -> Optional[Servicio]:
        if cedula in self.alquiler.keys():
            return self.alquiler[cedula]
        else:
            return None

    def reserva_vehiculo(self, cedula: str, hora_reserva: str, cantidad_personas: int, datos_tarjeta_bancaria: Optional[str], tipo_vehiculo: str):
        if self.buscar_reserva(cedula) is not None:
            if self.buscar_alquiler_vehiculo(cedula) is None:
                reserva_vehiculo: tuple = (Servicio(cedula, hora_reserva, cantidad_personas, datos_tarjeta_bancaria), tipo_vehiculo)
                self.alquiler[cedula] = reserva_vehiculo
            else:
                raise ObjetoExistente(f"Ya existe una reserva con la cédula {cedula}", cedula)
        else:
            raise ObjetoNoEncontrado(f"No existe una reserva con la cédula {cedula}", cedula)

    def buscar_reserva_salon_belleza(self, cedula) -> Optional[Servicio]:
        if cedula in self.belleza.keys():
            return self.belleza[cedula]
        else:
            return None

    def reserva_servicio_salon_belleza(self, cedula: str, hora_reserva: str, cantidad_personas: int, datos_bancarios: str):
        if self.buscar_reserva(cedula) is not None:
            if self.buscar_reserva_salon_belleza(cedula) is None:
                reserva_salon_belleza = Servicio(cedula, hora_reserva, cantidad_personas, datos_bancarios)
                self.belleza[cedula] = reserva_salon_belleza
            else:
                raise ObjetoExistente(f"Ya existe una reserva con la cédula {cedula}", cedula)
        else:
            raise ObjetoNoEncontrado(f"No existe una reserva con la cédula {cedula}", cedula)

    def reserva_servicio_lavanderia(self, cedula: str, hora_reserva: str):
        if self.buscar_reserva(cedula) is not None:
            reserva_servicio_lavanderia = Servicio(cedula, hora_reserva, None, None)
            self.lavanderia[cedula] = reserva_servicio_lavanderia
        else:
            raise ObjetoNoEncontrado(f"No existe una reserva con la cédula {cedula}", cedula)

    def servicio_check_out(self, cedula: str):
        if self.buscar_reserva(cedula) is not None:
            del self.checkin[cedula]
        else:
            raise ObjetoNoEncontrado(f"No existe una reserva con la cédula {cedula}", cedula)

    def servicio_limpieza_cuarto(self, cedula:str, hora_reserva: str):
        if self.buscar_reserva(cedula) is not None:
            reserva_servicio_limpieza = Servicio(cedula, hora_reserva, None, None)
            self.limpieza[cedula] = reserva_servicio_limpieza
        else:
            raise ObjetoNoEncontrado(f"No existe una reserva con la cédula {cedula}", cedula)

    def escribir_sugerencias(self, mensaje):
        self.sugerencias.append(mensaje)

