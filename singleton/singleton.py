"""
Nota: La diferencia entre cls y self es que cls se refiere a que el metodo pertenece
la clase, mientras self referencia a la instancia de la clase

El metodo __new__ se encarga de construir en este caso la unica instancia
mientras que el metodo __init__ la inicializa dandole valores
"""

def singleton (cls):

    instancias = dict()
    
    def wrap (*args, **kwatgs): #*args = Listado de argumentos, **kwatgs = diccionario de argumentos
        
        if cls not in instancias:
            instancias[cls] = cls (*args, **kwatgs)
        return instancias [cls]

    return wrap



@singleton
class paises (object):

    def __init__(self, pais):
         self.pais = pais


listapaises = ['Colombia', 'Venezuela', 'Cuba', 'Brazil', 'Israel', 'Portugal']
if __name__ == '__main__':  
    """
    if __name__ == '__main__': Es un codigo repetitivo que protege a los usuarios de invocar accidentalmente el script
    cuando no se tenia la intencion de hacerlo
    """
    
    
    usuario1 = paises(listapaises)
    usuario2 = paises('Venezuela')
    print(usuario1.pais)
    print(usuario2.pais)

    print(usuario1 is usuario2) #La palabra is se utiliza si se desea saber si un objeto es otro objeto