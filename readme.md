# ¿Qué es un patrón de diseño de Software?
> Los patrones de diseño son un conjunto de tecnicas, normas y herramientas que nos ayudan a producir software de alta claidad con un minimo esfuerzo # Actividad-Patrones-Arquitectonicos
### Conceptos Previos
#### Interfaces
> Las Interfaces son usadas para indicar qué métodos debe obligatoriamente implementar (contener) una Clase (aunque no tienen por qué comportarse del mismo modo).
> Una interfaz es un conjunto de métodos y propiedades que no tiene ninguna implementación. La implementación la va a hacer cada uno de los elementos que herede de la interfaz dependiendo de sus necesidades.

#### Modulo ABC
>Este módulo proporciona la infraestructura para definir clases de base abstracta (CBAs) en Python.

#### Clases Abstractas
> Son un tipo de clases en la que se pueden definir metodos y propiedades, pero no se puden instanciar de forma directa, es decir que estas clases se usan para construir  subclases y proporcionar una interfaz para estas, evitando la duplicacion de codigo.
> las clases abstractas define una interfaz común para las subclases. Proporciona atributos y métodos comunes para todas las subclases evitando así la necesidad de duplicar código. Imponiendo además lo métodos que deber ser implementados para evitar inconsistencias entre las subclases.

# Abstract factory
>Abstract factory es un metodo de patron de diseño creacional que tiene  como objetivo producir familias de objetos relacionados sin especificar sus clases concretas. Gracias a esto podemos producir de una forma mas facil y eficiente tipos similares de objetos.
>Para esto define una interfaz que se encarga de crear los productos distintos, pero deja la verdadera creacion de los objetos a clases de fabricas concretas

### Conclusion 
> El patron de diseño creacional abstract factory  tiene las funcionalidades y objetivos de:
>-Proporcionar una interfaz para crear familias de objetos relacionados o independientes sin especificar sus clases concretas 

### Cuando se debe aplicarlo?
>-Cuando el sistema debe ser independiante de como se crean sus objetos
>-Cuando en una familia de productos relacionados, estos estan diseñados para trabajar juntos
### Diagrama
![imagen](https://refactoring.guru/images/patterns/diagrams/abstract-factory/solution2.png)


# Command
> El command es un patron de diseño cuyo objetivo es convertir solicitudes u operaciones simples en objetos, gracias a este procedimientos se pueden hacer pasar solicitudes como argumentos de un metododo o poner en cola de ejecucion una solicitud, asi mismo estos objetos convertidos traeran consigo infromacion detallada acerca de los metodos y funcionalidades que se requieren para asi mejorar la eficiencia y funcionalidad.
 
 ### Diagrama
 ![imagen](https://refactoring.guru/images/patterns/diagrams/command/solution3-en.png)

 ### Ejemplo
 ![imagen](Patrones de Diseño\Imagenes\Command.png)


# Patron de Diseño Decorator 
> El patron de diseño Decoretor es un herramienta util y eficiente que permite a los desarrolladores modificar las funcionalidades y comportamientos de una funcion o clase. Esto lo hacen encapsulando una funcion para posteriormente extender o agregarle funcionamientos, sin modificarla permanentemente.
>Los Decorators las funciones se toman como argumento en otra funcion y posteriormente son  citadas dento de la funcion contenedora que modifica las funcionalidades

### Diagrama
![imagen](https://www.ionos.es/digitalguide/fileadmin/DigitalGuide/Schaubilder/representacion-grafica-del-patron-decorator.png)

### Ejemplo
![imagen](Patrones de Diseño\Imagenes\Decorator.png)

# Dependency injection
>El patron de Diseño es un principio que ayuda a disminuir el acoplamiento que significa cuando una clase necesita saber detalles internos sobre la estructura, informacion y funcionamiento de otra clase, atentando contra el principio de POO de modularizacion, ademas el patron Dependency injection insta en aumenta la cohesion y flexibilidad del codigo al momento de ser modificado y reestructurado

>Asi para implementar la Dependency injection se procura que los objetos ya no se creen unos a otros si no se se proporciones una fomma de inyectar dependencias en su lugar

>Con el patrón de inyección de dependencia, los objetos pierden la responsabilidad de ensamblar las dependencias. El absorbe esa responsabilidad.


# Factory

>El metodo factory o fabrica es una patron de diseño creativo que se encarga de crear objetos sin la necesidad de especificar sus clases.
>Para lograr este cometido, en vez de llamar al contructor __new__, define un metodo que crea los objetos
>Actualmente es un patron ampliamente usado en python ya que ofrece un alto nivel de flexibilidad para el codigo.
>El patron de diseño Factory sugiere el reemplazo de llamadas directas de construccion de objetos (__new__) con llamadas a un metodo de fabrica especial, esto no quiere decir que no so se crean utilizando el operador __new__ si no que se llaman desde el metodo de fabrica, generalmente los objetos devueltos por el metodo fabrica se llaman ***productos***

### Objetivo
>Su principal objetivo es evitar el acoplamiento entre clases, es decir, imagine que se tiene la clase Cliente y esta crea instancias relacionadas con la clase Proveedores, esto generara una dependencia y relacion entre amabas clases, que se denomina acoplamiento.
>Es decir que acoplamiento, significa cuando una clase necesita saber detalles internos sobre la estructura, informacion y funcionamiento de otra clase, atentando contra el principio de POO de modularizacion.
>Como se ha mencionado anteriormente el metodo factory consiste en la creacion de un subtipo de clase determinado por medio de una clase factory


#### Conclusion 
La fabrica produce objetos de una determinada clase, es decir que no hay que instanciar directamente, si no que por medio de la fabrica esta nos devolvera la instancia de la clase.

### Diagrama

![imagen](https://refactoring.guru/images/patterns/diagrams/factory-method/structure.png)

### Ejemplo
![imagen]()

# Facade Python 
> El patron de diseño estructural Facade permite la integracion de una interfaz unificada simplificada a un sistema complejo de clases, bibliotecas o marcos.
> Esto patron de diseño es una parte escencial de los Gang of Four. Por lo tanto proporciona una forma mas facil de acceder a los metodos de los sistemas subyacentes al proporcionar un unico punto de entrada.
### Diagrama
![imagen](https://refactoring.guru/images/patterns/diagrams/facade/structure.png)

### Ejemplo
![imagen](Patrones de Diseño\Imagenes\Facade.png)

# Memento
>Memento es un patron de diseño cuya funcionalidad consiste en capturar la informacion o estado de un objeto y guardarla mediante serializacion, para posteriormente restaurar u comparar el objeto guardado con el actual, cabe resaltar que no se busca comprometer o modificar la estructura e informacion del objeto requerido, simplemente guardarla


### Diagrama
![imagen](https://refactoring.guru/images/patterns/diagrams/memento/solution-en.png)


### Ejemplo
![imagen](Patrones de Diseño\Imagenes\Facade.png)


# Observer
> El patron de diseño Observer busca que los objetos notifiquen a otros objetos cuando estos sean alterados o sufran cambios en sus funcionalidades e informacion.
### Ejemplo Vida Real
> Para entender mejor este concepto supongamos que tenemos una tienda de aparatos electronicos que muy pronto recibira la ultima consola de videojuegos, asi los clientes estan muy ansiosos y realizan contantes viajes para comprobar si ya ha llegado el nuevo producto, lo mas logico de estos viajes es que sean perdidos y no tengan ninguna utilidad. Para esto el objeto interesante que en este caso es la tienda se le llamara  ***sujeto*** o tambien ***editor*** ya que avisara a los clientes que son llamados ***Suscriptores*** cuando llegue el ansiado producto.
>Asi mediante el patron observer se agregara un mecanismo de suscripcion a la tienda para que los clientes se suscriban si estan interesados en el producto, 


### Diagrama
![imagen](https://refactoring.guru/images/patterns/diagrams/observer/solution2-en.png)



### Ejemplo
![imagen](Patrones de Diseño\Imagenes\Observer.png)

# Patron de Diseño Prototype:
> Es un patron de diseño creacional que su principal objetivo es reducir el numero de clases usadas en las aplicaciones, mediante el clonamiento de objetos inclusive complejos, sin acoplarlos a sus clases especificas. Esto quiere decir que le permiten copiar objetos existentes independientemente de .
la implementacion concreta de sus clases.
## Ejemplo:
> Imaginen que se tiene la clase Figuras que produce diferentes figuras geometricas, como circulo, rectangulo, Triangulo, Cuadrado, Hexagono, etc. y todos estos son objetos. Posteriormente necesitamos crear un nuevo objeto aplicando las mismas funcionalidades de los objetos originales y copiara sus valores. Pero asi mismo no necesitamos copiar todos y cada uno de los campos del objeto original.
> Asi las clases prototipo deben tener una interfaz comun que permita copiar objetos incluso si se desconocen sus clases concretas.


### Diagrama
![imagen](https://refactoring.guru/images/patterns/diagrams/prototype/structure.png)




# Proxy
> Proxy es un Patron de Diseño que tiene la funcionalidad  de actuar como un intermediario que gestiona las solicitudes de los clientes que buscan un determinado recurso en otros servidores. 
>El patron proxy trata de proporcionar un objeto intermediario que represente o sustituya al objeto original con motivo de controlar el acceso y otras caracteristicas del mismo.

### Daigrama
![imagen](https://refactoring.guru/images/patterns/diagrams/proxy/solution-en.png)

### Ejemplo
![imagen](Patrones de Diseño\Imagenes\Proxy.png)

# Patron Singleton:
> El patron singleton es un patron de creacion enfocado en la creacion de objetos y tiene como objetivo la implementacion de una unica instancia cuando se realizan tareas repetitivas o de gran flujo de informacion. 
> Por lo tanto un singleton se aplica cuando con una unica instancia se puede realizar los procesos de creacion, inicializacion y acceso
### Ejemplo:
>Para contextualizar de mejor manera lo que permite hacer un Singleton, imagine que para un aeropuerto se necesita que los usuarios
elijan su pais de una determinada lista de paises, usualmente se podria realizar una instancia con la lista de los paises que lo conforman para cada usuario, como se podran dar cuenta una lista con cientos de elementos siendo instanciada para miles de usuarios es complejo repetitivo y poco eficiente, aqui entra el singleton que instanciando unicamente un elemento, que en este caso seria la lista de paises, los usuarios podrian acceder a ella de forma comun, es decir se crea una instancia unica la cual realize varias actividades y los usuarios puedan acceder a ella de manera globaL.

### Diagrama

![imagen](https://refactoring.guru/images/patterns/diagrams/singleton/structure-en.png)

### Ejemplo

![imagen](\Imagenes\Singleton.png)

# Strategy 
> El patron de diseño de comportamiento Strategy tiene como objetivo definir una serie de algoritmos encapsulados que permite colocar cada uno de ello en una clase separada y hacer sus objetos intercambiables.
> Se implementa en Python reemplazando dinámicamente el contenido de un método definido dentro de una clase con el contenido de funciones definidas fuera de la clase. Permite seleccionar el algoritmo en tiempo de ejecución. Este método también se denomina Método de política.

### Diagrama
![imagen](https://refactoring.guru/images/patterns/diagrams/strategy/solution.png)


### Ejemplo
![imagen](Imagenes\Strategy.png)