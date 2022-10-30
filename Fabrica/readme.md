# Factory

>El metodo factory o fabrica es una patron de diseño creativo que se encarga de crear objetos sin la necesidad de especificar sus clases.
>Para lograr este cometido, en vez de llamar al contructor __new__, define un metodo que crea los objetos
>Actualmente es un patron ampliamente usado en python ya que ofrece un alto nivel de flexibilidad para el codigo.
>El patron de diseño Factory sugiere el reemplazo de llamadas directas de construccion de objetos (__new__) con llamadas a un metodo de fabrica especial, esto no quiere decir que no so se crean utilizando el operador __new__ si no que se llaman desde el metodo de fabrica, generalmente los objetos devueltos por el metodo fabrica se llaman ***productos***

### Objetivo
>Su principal objetivo es evitar el acoplamiento entre clases, es decir, imagine que se tiene la clase Cliente y esta crea instancias relacionadas con la clase Proveedores, esto generara una dependencia y relacion entre amabas clases, que se denomina acoplamiento.
>Es decir que acoplamiento, significa cuando una clase necesita saber detalles internos sobre la estructura, informacion y funcionamiento de otra clase, atentando contra el principio de POO de modularizacion.
>Como se ha mencionado anteriormente el metodo factory consiste en la creacion de un subtipo de clase determinado por medio de una clase factory


 