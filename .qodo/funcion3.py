#crear una funcion que resiva una lista de nu eros enteros 
# y calcule su promedio para retornarlos

#def calcular_promedio (listaNumeros):
 #   numero= []
  #  if len(listaNumeros) == 0:
   #     return 0
    #for i in listaNumeros:
     #   numero.append(i)
    #promedio = sum(numero) / len(numero)
    #return promedio

#como recorrer una lista en pythoon

def calcular_promedio (notas):
 suma=0
 for nota in notas:
  suma+=nota
  promedio=suma/len(notas)
 return promedio    
  print(nota)

notaas=[1,2,3,4,5]
print(calcular_promedio(notaas))
