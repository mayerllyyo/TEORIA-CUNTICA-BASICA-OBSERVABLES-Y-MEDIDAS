# TEORIA CUANTICA BASICA OBSERVABLES Y MEDIDAS
Este repositorio contiene ejemplos y problemas resueltos relacionados con conceptos básicos de computación cuántica. Se incluyen implementaciones en Python utilizando la biblioteca NumPy para cálculos numéricos y manipulación de matrices.

Contenido
El repositorio está organizado en diferentes secciones:

Teoría Cuántica Básica: Aquí se encuentran ejemplos relacionados con observables, medidas y probabilidades en sistemas cuánticos.

Retos de Programación del Capítulo 4: Incluye ejercicios y soluciones del capítulo 4 del libro, que cubre temas como la amplitud de transición, matrices de observables, valores y vectores propios, y la dinámica de sistemas cuánticos.

Problemas Adicionales: Sección donde se encuentran problemas adicionales para practicar y discutir.

Bibliotecas necesarias
Para ejecutar los ejercicios y problemas en este repositorio, necesitarás tener instalada la biblioteca Python NumPy, Python jupyter y  Python math  . Puedes instalarla utilizando pip:
```python
pip install numpy
pip install jupyter
pip install math
```
## Función "Complex" en python.
La función complex devuelve un número imaginario a partir de valores cedidios como argumentos.
La parte derecha de nuestro argumento se interpreta como parte imaginaria.
tupla (a,b) -> (a, bj)
 
# Función #1
El sistema debe calcular la probabilidad de encontrarlo en una posición en particular.
- Definimos el vector V1
- Definimos la posición donde queremos encontrar la posibilidad.
- Mediante la función "np.linalg.norm(v1)" propia de Nuympy encontramos la norma del vector.
- Definimos la posición como la variable "p"
- Para encontrar el valor en esa posición utilizamos v1[p]
- Definimos la operación como el valor absoluto de la posición elevado al cuadrado sobre la norma del vector al cuadrado.

# Función #2
El sistema si se le da otro vector Ket debe buscar la probabilidad de transitar del primer vector al segundo.
- Definimos el vector V2
- Definimos el vector V3
- Encontramos el Bra del ket de llegada, utilizamos las funciones propias de Numpy "np.transpose(np.conjugate(v3))"
- Definimos nuevamente nuestros vectores como Vector / norma del vector  (La norma del vector se puede encontrar con la función propia de Numpy np.linalg.norm(v))
- Definimos la operación como el producto interno entre el vector al que le encontramos el Bra y el vector de salida"

# Función #1 (Retos de programación)
El sistema debe calcular la amplitud de transicion, recibiendo dos vectores.
- Definimos dos vectores.
- Normalizamos los vectores mediante la función "np.linalg.norm(v4)"
- A nuestro vector de llegada realizamos el conjugado mediante la funcióm "np.conjugate(np.transpose(v5))" calculando asi el conjugado y el transpuesto.
- Realizamos producto punto punto entre el vector de llegada calculado anteriormente con el vector de salida V4, luego lo dividimos entre la multiplicación de las normas.

# Función #2 (reto de programación)
El sistema debe verificar que el observable es una matriz hermitiana, esto se realiza mediante la función "np.transpose(np.conjugate(Observable))" si este resultado es igual al observable original continua con el proceso de calcular la media y varianza, si no, se da por terminado.
- Realizamos producto punto  entre el observable y nuestro ket.
- A la operación anterior le calculamos la adjunta transpuesta.
- luego realizamos el producto punto entre la operacion definida anteriormente y nuevamente nuestro ket original; asi obtendremos el valor esperado.
- Para continuar con el proceso de calcular la varianza tomamos nuestro observable origiginal y lo restamos con el valor esperado multiplicado por la identidad.
- De la operación anterior obtendremos una matriz nueva, esta matriz la multiplicaremos por si misma.
- A nuestro ket original le encontramos el conjugado y la transpuesta y lo multioplicamos con el resultado anterior que es una matriz.
- A este resultado lo multiplicamos por el ket original y obtendremos la varianza.

# Función #3 (reto de programación)
El programa debe calcular los valores propios y vectores propios del observable; ademas de eso la probabilidad de transición entre los vectores propios despues de la observación.
- Definimos nuestro observable y el estado inicial.
- Calculamos los valores propios y vectores propios mediante la funcion "np.linalg.eig(observable)"
- Normalizamos nuestros vectores propios
- Para calcular la propabilidad de transicion utilizamos la funcion "np.abs(np.dot(normalizados.T.conj(), estado))**2" -> .T realiza la transpuesta y .conj el conjugado.

# Función #4 (reto de programación)
- Definimos nuestro estado inicial y dos mastrices mas del mismo tamaño.
- Realizamos el producto punto entre el estado inicial y nuestra primera matriz
- realizamos el producto punto entre la matriz numero 2 y el resultado obtenido anteriormente.

## Como se deben ejecutar las pruebas.
Las pruebas se deben ejecetar primero llamando la libreria unitest, a partir de ahi seguimos el procedimiento de llamar 
nuesta función de la libreria pasada. a partir de ahi definimos nuestras variables a utilizar y el valor que deseamos 
esperar, definimos la operación y al final citamos "np.testing.assert_almost_equal (operación, valor esperado)"
