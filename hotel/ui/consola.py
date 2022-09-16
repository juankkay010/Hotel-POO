import sys
from hotel.mundo.hotel import Hotel


class Consola:

    def __init__(self):
        self.hotel = Hotel()
        self.opciones = {
            "1": self.realizar_reserva,
            "2": self.registrar_usuario,
            "3": self.cancelar_reserva,
            "4": self.reserva_restaurante,
            "5": self.salir
        }

    def mostrar_menu(self):
        print("""
            \n
            BIENVENIDO A EL HOTEL POO
            ===================================
            Menú de opciones:\n
            1. Realizar reserva
            2. Registrar usuario
            3. Cancelar reserva
            4. Reservar restaurante
            5. Salir
            
            ===================================
            """)

    def registrar_usuario(self):
        print("\n>>> REGISTRAR USUARIO")
        cedula = input("Ingrese la cédula: ")
        nombre = input("Ingrese el nombre: ")
        fecha_nacimiento = input("Ingrese la fecha de nacimiento: ")
        numero_habitacion = input("Ingrese el número de habitación: ")
        if self.hotel.registrar_usuario(cedula, nombre, fecha_nacimiento, numero_habitacion):
            print("INFO: El usuario se registró exitosamente")
        else:
            print(f"ERROR: Ya existe un usuario con la cédula {cedula}")

    def realizar_reserva(self):
        print("\n>>> REALIZAR RESERVA")
        cedula = input("Ingrese la cédula del encargado de la reserva: ")
        nombre = input("Ingrese su nombre: ")
        cantidad_noches = int(input("Ingrese la cantidad de noches de estadía: "))
        cantidad_personas = int(input("Ingrese la cantidad de personas que harán parte de la reserva: "))
        numero_habitacion = self.hotel.numero_habitacion
        if self.hotel.realizar_reserva(cedula, nombre, cantidad_noches, cantidad_personas):
            print(f"INFO: La reserva se ha completado exitosamente y su número de habitación es {numero_habitacion} ")
        else:
            print("INFO: No se pudo completar la reserva ya que la cédula ingresada se encuentra registrada")

    def cancelar_reserva(self):
        print("\n>>> CANCELAR RESERVA")
        cedula = input("Ingrese la cédula del encargado de la reserva: ")
        if self.hotel.cancelar_reserva(cedula):
            print(f"INFO: La reserva ha sido cancelada con exito")
        else:
            print(f"INFO: La reserva no ha podido ser cancelada")

    def reserva_restaurante(self):
        print("\n>>> REALIZAR RESERVA DE RESTAURANTE")
        cedula = input("Ingrese la cédula del encargado de la reserva: ")
        hora_reserva = input("Ingrese la hora de la reserva: ")
        cantidad_personas = int(input("Ingrese la cantidad de personas que asistirán a la reserva: "))
        if self.hotel.reservar_restaurante(cedula, hora_reserva, cantidad_personas):
            print(f"INFO: La reserva se ha completado exitosamente")
        else:
            print(f"INFO: No se pudo completar la reserva ya que la cédula ingresada no se encuentra registrada")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion is not None:
                accion()
            else:
                print(f"ERROR: {opcion} no es una opción válida")

    def salir(self):
        print("\nMUCHAS GRACIAS POR USAR NUESTRA APLICACIÓN")
        sys.exit(0)
