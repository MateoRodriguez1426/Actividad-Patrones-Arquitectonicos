def funcion_decoradora(funcion_parametro):
    def funcion_interior():

        #Acciones adiccionales que decoran

        print("Vamos a realizar un calculo")
        funcion_parametro()

        #Acciones adicionales que decoran
        print("Hemos terminado el calculo")
    return funcion_interior

@funcion_decoradora
def suma ():
    print(15+23)


@funcion_decoradora
def resta():
    print(78-54)

suma()
resta()