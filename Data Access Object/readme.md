# Data Access Object
> El Data Access Object o patron DAO se utiliza en las API para separar el servicio de acceso de datos de bajo nivel de los servicios comerciales de alto nivel 
### Ventajas
>1. La ventaja de usar objetos de acceso a datos es la separación relativamente simple y rigurosa entre dos partes importantes de una aplicación que pueden pero no deben saber nada entre sí, y que se puede esperar que evolucionen con frecuencia e independientemente.

>2. Si necesitamos cambiar el mecanismo de persistencia subyacente, solo tenemos que cambiar la capa DAO y no todos los lugares en la lógica del dominio desde donde se usa la capa DAO.