# =======================================
# ========== Abstracción ================
# =======================================
# La abstracción es un principio de la programación orientada a objetos
# que consiste en ocultar los detalles complejos de implementación y

from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    
    @abstractmethod
    def calcular_area(self):
        pass
    
class Circulo(FormaGeometrica):
    def __init__(self, radio):
        self.radio = radio
        
    def calcular_area(self):
        return 3.1416 * (self.radio ** 2)