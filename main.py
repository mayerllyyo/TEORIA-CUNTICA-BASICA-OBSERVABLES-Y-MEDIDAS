
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
