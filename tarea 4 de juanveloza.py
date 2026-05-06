import logging
from abc import ABC, abstractmethod


# Se encarga de registrar errores en un archivo externo para mantener la estabilidad.
logging.basicConfig(
    filename='software_fj_errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
class SoftwareFJError(Exception):
    """Clase base para excepciones del sistema."""
    pass

class ReservaInvalidaError(SoftwareFJError):
    """Se lanza cuando los parámetros de una reserva son incorrectos."""
    pass

class ServicioNoDisponibleError(SoftwareFJError):
    """Se lanza cuando un servicio solicitado no está activo o disponible."""
    pass