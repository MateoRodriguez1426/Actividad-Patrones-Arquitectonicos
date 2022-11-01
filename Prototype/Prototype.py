import copy

class claseDireccion ():
    def __init__ (self, direccion, ciudad):
        self.direccion = direccion
        self.ciudad = ciudad
    """
    Este método devuelve la representación de cadena del objeto. Este método se llama 
    cuando se print()invoca str()una función en un objeto. 
    Este método debe devolver el objeto String. 
    
    """
    def __str__(self):
        return f'{self.direccion}, {self.ciudad}'
    
class empleado ():
        def __init__ (self, nombre, cedula, direccion):
            self.nombre = nombre
            self.cedula = cedula
            self.direccion=direccion 

        def __str__(self):
            return f'{self.nombre}, {self.direccion}'
 
class empleadoFabrica ():
    empleadouno = empleado('', cedula=(21314564), direccion=('Carrera 98 #65bis-76', 'Bogota D.C'))
    empleadodos = empleado('', cedula=(51814502), direccion=('Carrera 110 #22 Sur- 12', 'Bogota D.C'))


    @staticmethod
    def __nuevoempleado (proto, nombre, Lugarresidencia):
        nuevo = copy.deepcopy(proto)
        nuevo.nombre = nombre
        nuevo.direccion.ciudad = Lugarresidencia
        return nuevo

    @staticmethod
    def nuevoempleadouno (nombre, Lugarresidencia):
        return empleadoFabrica.__nuevoempleado(
        empleadoFabrica.empleadouno, nombre, Lugarresidencia
        )

    @staticmethod
    def nuevoempleadodos (nombre, Lugarresidencia):
        return empleadoFabrica.__nuevoempleado(
        empleadoFabrica.empleadodos, nombre, Lugarresidencia
        )


Julian = empleadoFabrica.nuevoempleadouno('Julian', 'Carrera 14 #32-17 Bogota D.C')
Maradona = empleadoFabrica.nuevoempleadodos('Maradona', 'Carrera 72 #12-09 Bogota D.C')


print(Julian)
print(Maradona)