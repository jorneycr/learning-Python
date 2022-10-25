#ABC = Abstract Base Class
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        if 0 < ancho < 10:
            self._ancho = ancho
        else:
            self._ancho = 0
        if 0 < alto < 10:
            self._alto = alto
        else:
            self._alto = 0

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        self._alto = alto

    @abstractmethod
    def calcularArea(self):
        pass

    def __str__(self):
        return f'Figura Geometrica: {self._ancho} {self._alto}'

