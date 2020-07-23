## ¿Qué son las pruebas unitarias?
¿Código que prueba otro código? sí, pero con el objetivo de asegurar que nuestro programa haga lo que se espera que haga y lo haga bien.

Cada prueba unitaria, caso de uso o conjunto de datos se puede interpretar como parte de un checklist de cumplimiento.

## ¿Cómo pueden ahorrarnos tiempo de desarrollo?
Existe cierta resistencia como desarrolladores en ~~perder~~ dedicar tiempo a crear pruebas unitarias porque es trabajo adicional, pero es mucho más rápido ejecutar una prueba que estar ingresando manualmente valores en un formulario, en postman, siguiendo un flujo de interacción, etc

## ¿Cuando hacer pruebas unitarias?
- Cuando la tarea o funcionalidad tiene un alto grado de complejidad
- Cuando el tiempo de hacer pruebas manuales es mayor al tiempo que tardaríamos en automatizar esa prueba
- Cuando existen muchos casos de uso

## ¿Cómo afecta o ayuda en el mantenimiento del código?
Por un lado nos ayuda a validar que todo sigue funcionando como se planeó anteriormente, por otro lado nos ayuda a probar nuevos casos de uso no previstos.

## ¿Cómo ayuda al proceso de análisis?
Nos obliga pensar en la información / datos / variables que necesitamos de entrada y valores / información / cálculos de salida, ya sea en forma de variables o como registros en la base de datos.

## ¿Qué tipo de cosas no deberíamos probar?
- Funcionalidad propia del framework o librería que estemos usando, tienen sus propias pruebas unitarias
- Funcionalidad de baja complejidad

## ¿Qué otras ventajas tiene hacer pruebas unitarias?
Nos empuja a desarrollar funciones o componentes con [alta cohesión y bajo acoplamiento](https://www.codesolt.com/tutoriales/fundamentos/alta-cohesion-bajo-acoplamiento), porque al crear las pruebas unitarias necesitamos no depender de otros componentes y sobre todo porque no tenemos una interfaz de usuario que ingrese los datos.

Hasta cierto punto nos ayudan como documentación, porque están plasmados los casos de uso para los que fue diseñado el código

Idealmente con herramientas de integración continua nos daría alertas o feedback sobre los cambios que hacemos en el código, lo que nos da cierto grado de confianza o seguridad para liberar nuevo código.

## ¿Cómo es desarrollar sin pruebas unitarias?
Hacemos cambios con la esperanza de que no estamos rompiendo algo en otro lado, ¿por que? porque probar código previamente probado y liberado implica dedicar el mismo tiempo para probar que se le dedico en su momento.

## ¿Nice to have? ¿Must to have?
Depende de cada situación y el valor de retorno que podríamos obtener al invertir tiempo y esfuerzo en hacer pruebas unitarias o de integración
