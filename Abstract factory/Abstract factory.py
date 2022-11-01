from abc import ABC, abstractmethod

#ESTA ES LA FABRICA ABSTRACTA
class Fabrica (ABC):

    @abstractmethod
    def crear_televisor (self):
        pass

    @abstractmethod
    def crear_celular(self):
        pass


#La super()función se utiliza para dar acceso a métodos y propiedades de una clase principal o hermana.

#Esto es una fabrica concreta
class Apple (Fabrica):
    def crear_televisor(self):
        return televisorApple()

    def crear_celular(self):
        return celularApple()

#Esto es una fabrica concreta
class Sony (Fabrica):
    def crear_televisor(self):
        return televisorSony()
    def crear_celular(self):
        return celularSony()


#A partir de aqui se implementaran los productos correspondientes


#Producto televisor
class televisor(ABC):
    @abstractmethod
    def Televisorfuncion (self):
        pass


class televisorSony(televisor):
    def Televisorfuncion(self):
        return "Televisor Bravia XR 2022" 

class televisorApple(televisor):
    def Televisorfuncion(self):
        return "Televisor Apple TV 4K" 

#Producto Celular
class celular(ABC):
    @abstractmethod
    def celularfuncion (self):
        pass


class celularApple(celular):
    def celularfuncion(self):
        return "Iphone 7 Plus 32Gb"

class celularSony(celular):
    def celularfuncion(self):
        return "Sony Xperia plus 16Gb Ram"

class Cliente:
    def codigoCliente (self, Fabrica):
        televisor = Fabrica.crear_televisor()
        celular = Fabrica.crear_celular()

        print(televisor.Televisorfuncion())
        print(celular.celularfuncion())


if __name__ == '__main__':
    c = Cliente()
    print("Fabrica Sony: ")
    c.codigoCliente(Sony())
    print('\n')
    print("Fabrica Apple: ")
    c.codigoCliente(Apple())
    print('\n')


