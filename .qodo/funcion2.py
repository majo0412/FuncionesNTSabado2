#crear una funcion que de forma aleatoria crea un alista de n 
#nota s(entregar) y devuelve la list

import random
def crear_lista_aleatoria(n):
    notas = []
    for i in range(n):
        nota=random.randint(1, 5)
        notas.append(nota)
    return notas