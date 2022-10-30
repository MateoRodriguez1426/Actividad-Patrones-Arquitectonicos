# Patron de Diseño Prototype:
> Es un patron de diseño creacional que su principal objetivo es reducir el numero de clases usadas en las aplicaciones, mediante el clonamiento de objetos inclusive complejos, sin acoplarlos especificos. Esto quiere decir que le permiten copiar objetos existentes independientemente de .
la implementacion concreta de sus clases.
## Ejemplo:
> Imaginen que se tiene la clase Figuras que produce diferentes figuras geometricas, como circulo, rectangulo, Triangulo, Cuadrado, Hexagono, etc. y todos estos son objetos. Posteriormente necesitamos crear un nuevo objeto aplicando las mismas funcionalidades de los objetos originales y copiara sus valores. Pero asi mismo no necesitamos copiar todos y cada uno de los campos del objeto original.
> Asi las clases prototipo deben tener una interfaz comun que permita copiar objetos incluso si se desconocen sus clases concretas.


