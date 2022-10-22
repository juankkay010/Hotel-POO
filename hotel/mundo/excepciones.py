class HotelError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje


class ReservaExistente(HotelError):

    def __init__(self, mensaje, cedula):
        super.__init__(mensaje)
        self.cedula = cedula



