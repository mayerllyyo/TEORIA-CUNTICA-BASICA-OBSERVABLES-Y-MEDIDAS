# Función para calcular los valores propios y vectores propios
def calcular_valores_vectores_propios(m):
    # Calcular los valores propios y vectores propios
    valores_propios, vectores_propios = np.linalg.eigh(m)
    return valores_propios, vectores_propios

# Función para calcular la probabilidad de transitar a un vector propio específico
def calcular_probabilidad_transicion(v1, v2):
    # Normalizar los vectores
    v1_norm = v1 / np.linalg.norm(v1)
    v2_norm = v2 / np.linalg.norm(v2)
    # Calcular el producto interno de los vectores normalizados
    producto_interno = np.abs(np.vdot(v1_norm, v2_norm))
    # Calcular la probabilidad de transición
    probabilidad_transicion = np.abs(producto_interno) ** 2
    return probabilidad_transicion

# Ejemplo de uso
# Matriz hermitiana de ejemplo
m = np.array([[1, 2+1j, 3], [2-1j, 4, 5+2j], [3, 5-2j, 6]])

# Calcular los valores propios y vectores propios
valores_propios, vectores_propios = calcular_valores_vectores_propios(m)

# Imprimir los valores propios y vectores propios
print("Valores propios:", valores_propios)
print("Vectores propios:")
print(vectores_propios)

# Vector de ejemplo
v = np.array([1, 2, 3])

# Calcular la probabilidad de transitar a cada vector propio después de la observación
probabilidades_transicion = []
for vector_propio in vectores_propios.T:  # Iterar sobre los vectores propios transpuestos
    probabilidad = calcular_probabilidad_transicion(v, vector_propio)
    probabilidades_transicion.append(probabilidad)

# Imprimir las probabilidades de transición
for i, probabilidad in enumerate(probabilidades_transicion):
    print("Probabilidad de transitar al vector propio", i+1, ":", probabilidad)





import numpy as np

# Función para calcular el estado final del sistema
def estado_final(U_n_series, estado_inicial):
    estado_actual = estado_inicial
    for U_n in U_n_series:
        estado_actual = np.dot(U_n, estado_actual)
    return estado_actual

# Ejemplo de uso
# Definir las matrices de evolución temporal U_n
U_1 = np.array([[1, 0], [0, 1]])  # Por ejemplo, una matriz de identidad
U_2 = np.array([[0, 1], [1, 0]])  # Por ejemplo, una matriz de intercambio
U_3 = np.array([[1, 1], [1, -1]]) # Por ejemplo, una matriz de Hadamard

# Serie de matrices de evolución temporal
U_n_series = [U_1, U_2, U_3]

# Estado inicial del sistema
estado_inicial = np.array([1, 0])  # Por ejemplo, estado inicial |0⟩

# Calcular el estado final del sistema
estado_final_sistema = estado_final(U_n_series, estado_inicial)

# Imprimir el estado final del sistema
print("Estado final del sistema:")
print(estado_final_sistema)








def hermitiana_media_varianza(m,v):
    # Función para calcular el conjugado de un vector complejo
    def b(v):
        for i in range(len(v)):
            v[i] = v[i].conjugate()
        return v
        
    # Función para calcular la acción de una matriz sobre un vector
    def accion(v, m):
        ans = [0] * len(m)
        for i in range(len(m)):
            aux = 0
            for j in range(len(m[i])):
                aux += m[i][j] * v[j]
            ans[i] = aux
        return ans
        
    # Función para calcular el producto interno entre dos vectores
    def prod_inter(v1, v2):
        ans = 0
        for i in range(len(v1)):
            v1[i] = v1[i].conjugate()
            ans += v1[i] * v2[i]
        return ans
    # Función para calcular el producto de dos matrices        
    def prod_mat(m1, m2):
            ans = [[0 for j in range(len(m2[0]))] for i in range(len(m1))]
            for i in range(len(m1)):
                for j in range(len(m2[0])):
                    aux = 0
                    for k in range(len(m2)):
                        aux = m1[i][k] * m2[k][j]
                    ans[i][j] = aux
            return ans
    b_v=b(v)
    ax_v=accion(v,m)
    media=prod_inter(ax_v,b_v)
    matri=[[media * -1 for i in range(len(m[0]))] for j in range(len(m))]
    for i in range(len(m)):
        for j in range(len(m)):
            matri[i][j] += m[i][j]
    matriz=prod_mat(matri,matri)
    var=prod_inter(accion(v,matriz),b_v)
    return media,var
# Ejemplo de uso de la funcion hermitiana_media_varianza
v = np.array([1, 2, 3])  
m = np.array([[1, 0, 0], [0, 2, 0], [0, 0, 3]])  

m = [[1, 2+1j, 3], [2-1j, 4, 5+2j], [3, 5-2j, 6]]
v = [1, 2, 3]
# Calcular la media y la varianza
media, varianza = hermitiana_media_varianza(m, v)
# Imprimir resultados
print("La media del observable es:", media)
print("La varianza del observable es:", varianza)







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
