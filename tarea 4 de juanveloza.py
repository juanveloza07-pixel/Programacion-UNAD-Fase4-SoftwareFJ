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
class EntidadSistema(ABC):
    """Clase abstracta para representar entidades generales del sistema."""
    
    @abstractmethod
    def obtener_detalles(self):
        """Método obligatorio para todas las clases derivadas."""
        pass
def ejecutar_simulacion_operacion(datos_reserva):
    """
    Simula una operación de gestión con bloques try/except/else/finally.
    Implementa encadenamiento de excepciones.
    """
    try:
        print("\n--- Iniciando Proceso de Gestión ---")
        
        # Validación de ejemplo (Esto será reemplazado por la lógica de tus compañeros)
        if not datos_reserva:
            raise ValueError("Los datos de la reserva están vacíos.")
            
        if datos_reserva.get("dias", 0) <= 0:
            # Encadenamiento de excepciones: de ValueError a ReservaInvalidaError[cite: 2]
            raise ReservaInvalidaError("La duración debe ser mayor a 0 días.")
            
        print("Validando disponibilidad del servicio...")
        
    except ReservaInvalidaError as e:
        # Registro en el archivo de logs[cite: 2]
        logging.error(f"Error en validación: {e}")
        print(f"ALERTA: No se pudo procesar la reserva. Detalle: {e}")
        
    except Exception as e:
        # Captura cualquier otro error inesperado para evitar que el programa se cierre[cite: 2]
        logging.critical(f"Fallo crítico inesperado: {e}")
        # Re-lanzamos con una excepción personalizada (encadenamiento)[cite: 2]
        raise SoftwareFJError("Ocurrió un fallo técnico interno.") from e
        
    else:
        # Se ejecuta solo si NO hubo errores
        print("Operación completada exitosamente.")
        logging.info("Operación exitosa registrada.")
        
    finally:
        # Se ejecuta siempre, haya error o no
        print("Cerrando sesión de usuario y limpiando recursos...")