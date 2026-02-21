#como crear 200 listas de 1 a 5 pythoon sin pedir los datos al usuario
#sin que mas los datos manueales
import random
notas=[]
for i in range(5):
        
        nota=random.randint(1,5)
        print(nota)
        notas.append(nota)

notas.insert(0, 10) #agrega un elemento al inicio de la lista
notas.insert(3, 8) #agrega un elemento en la posicion 3 de la lista
notas.remove(3) #elimina el elemento 3 de la lista
notas.pop(0) #elimina el elemento en la posicion 0 de la lista
notas.sort() #ordena la lista de menor a mayor
notas.clear()#elimina todos los elementos de la lista
print(notas)
      