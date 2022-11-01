
import os
from abc import ABC, abstractmethod
from typing_extensions import Self
from unittest import result
class Servidor (ABC):
    @abstractmethod
    def descargar (self, url):
        pass


class Miservidor(Servidor):
    def __init__(self,puerto ,host):
        self.puerto = puerto
        self.host = host


    def descargar(self, url):
        return "Descargando Para " + self.host
 

class ProxyMiServidor(Servidor):
    def __init__ (self, puerto, host):
        self.puerto = puerto
        self.host = host
        self.miServidor = None
    def descargar(self, url):
        if (self.validar(url)):
            if(self.miServidor == None):
                self.miServidor = Miservidor(self.puerto, self.host)
                resultado = self.miServidor.descargar(url)
            else:
                resultado = "Desde "+ self.host + "no puedes descargar"

            return resultado


    def validar(self, url):
        if (url == r'C:\Users\MATEO\OneDrive\Documentos\PYTHON\Patrones de Diseño\Proxy\david'):
            return True
        return False 


path = os.getcwd()
program = ProxyMiServidor(3434, 'David')
print (path)
result = program.descargar(path)
print (result)