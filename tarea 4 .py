import logging
from abc import ABC, abstractmethod
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='sistema_reservas.log',
    filemode='a'
)
