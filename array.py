from algo1 import *

#SEARCH
def search(array,elemento) :
  #inicializo variable
  indice = None

  for i in range(0,len(array)) :
    if array[i] == elemento :
      indice = i
      break

  return indice

#INSERT
def insert(array,elemento,posicion) :
  #calculo dimension del array
  dimension = len(array)

  if posicion >= dimension or posicion < 0 :  #analiza si la posicion se encuentra en el vector
    posicion = None 
  else :
    for i in range(dimension-1,posicion,-1) :
     array[i] = array[i-1]
    array[posicion] = elemento 

  return posicion

#DELETE
def delete(array,elemento) :
  #calculo dimension del array
  dimension = len(array)
  posicion = search(array,elemento)

  if posicion != None :
    for i in range(posicion,dimension-1) :
      array[i] = array[i+1]
    array[dimension-1] = None 
    
  print(array)  
  return posicion  

#LENGTH
def length(array) :
  contador = 0
  for i in range(0,len(array)) :
    if array[i] != None :
      contador = contador + 1
  return contador

#Imprime matriz 
def print_matrix(array,m,n):
  print("{")
  for i in range(0,m):
    for j in range(0,n):
      print(array[i][j], end = " ")
    print("")  
  print("}")    