
import numpy as np
# probabilidad de encontrarlo en una posición en particular.
def probabilidad_pos(v, p):
    norma = np.linalg.norm(v) ** 2
    if p < 0 or p >= len(v):
        raise ValueError("La posición especificada está fuera del rango.")
    c = (abs(v[p]))**2
    print(f"La probabilidad de encontrar la partícula en la posición {p} es: {c/norma}")
    return c/norma
#
def probabilidad_transitar(v, k):

    nv = np.linalg.norm(v)
    nk = np.linalg.norm(k)
    for i in range(len(v)):
        v[i] = v[i] / nv
        k[i] = k[i] / nk

    prod_in = 0
    for i in range(len(v)):
        prod_in+= np.conj(k[i])*v[i]

    prod_v = nv * nk
    prob = prod_in / prod_v
    return prob
probabilidad_pos([-3-1j,-2j,1j,2],2)

print(probabilidad_transitar([1-3j,2,3,4,2],[9,1,8,7,6]))


# Definimos la función transicion que toma dos vectores v1 y v2 como entrada
def ampl_transicion(v1, v2):  
    norma_v1 = np.linalg.norm(v1)  # Calcula la norma del vector v1
    norma_v2 = np.linalg.norm(v2)  # Calcula la norma del vector v2

    # Normaliza el vector v1 dividiendo cada componente por su norma
    for i in range(len(v1)):
        v1[i] = v1[i] / norma_v1

    # Normaliza el vector v2 dividiendo cada componente por su norma
    for i in range(len(v2)):
        v2[i] = v2[i] / norma_v2

    # Calcula el conjugado de cada componente del vector v1
    for i in range(len(v1)):
        v1[i] = v1[i].conjugate()

    # Calcula el producto interno de los vectores normalizados
    interno = np.inner(v1, v2)

    # Devuelve el cuadrado del valor absoluto del producto interno como la probabilidad de transición
    return np.abs(interno) ** 2

# Ejemplo de uso de la función transicion
v1 = np.array([1+2j, -3j, 4+1j])  # Definición del primer vector complejo v1
v2 = np.array([5j, 2-1j, 3+4j])    # Definición del segundo vector complejo v2

# Llama a la función transicion con los vectores v1 y v2, y almacena el resultado en 'probabilidad'
probabilidad = ampl_transicion(v1, v2)

# Imprime la probabilidad de transitar de v1 a v2
print("La probabilidad de transitar de v1 a v2 es:", probabilidad)
