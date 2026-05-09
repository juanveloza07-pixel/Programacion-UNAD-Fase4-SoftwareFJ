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