import logging
from abc import ABC, abstractmethod
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='sistema_reservas.log',
    filemode='a'
)
class ReservaError(Exception):
    """Clase base para excepciones del sistema."""
    pass

class ValidacionDatoError(ReservaError):
    """Error cuando un dato ingresado no cumple el formato o rango."""
    pass
class Cliente:
    def __init__(self, nombre, id_cliente):
        self.__nombre = nombre  # Encapsulamiento
        self.__id_cliente = id_cliente

    @property
    def nombre(self):
        return self.__nombre

class Servicio(ABC):
    """Clase abstracta que demuestra herencia y polimorfismo."""
    def __init__(self, nombre_servicio, costo_base):
        self._nombre_servicio = nombre_servicio
        self._costo_base = costo_base

    @abstractmethod
    def calcular_costo(self):
        """Método abstracto para ser sobrescrito (Polimorfismo)."""
        pass

class ReservaSala(Servicio):
    def __init__(self, horas):
        super().__init__("Reserva de Sala", 50.0)
        if horas <= 0:
            raise ValidacionDatoError("Las horas deben ser mayores a cero.")
        self.__horas = horas

    def calcular_costo(self):
        # Sobrescritura de método
        return self._costo_base * self.__horas

