from algo1 import *

class LinkedList:
  head = None

class Node:
  value = None
  nextNode = None

def escritura(L):
  currentNode = L.head
  while currentNode != None:
    print(currentNode.value)
    currentNode = currentNode.nextNode


#ADD #Complejidad: O(1)   
def add(L,element):
  new_node = Node()
  new_node.value = element
  new_node.nextNode = L.head
  L.head = new_node

#SEARCH #Complejidad: O(n)
def search(L,element):  
  currentNode = L.head
  position = None
  i = 0

  while currentNode != None:
    if currentNode.value == element:
      position = i
      break
    i = i + 1
    currentNode = currentNode.nextNode

  return position  

"""
Alternativa
def search(L,element):
  currentNode = L.head
  position = None
  dimension = length(L)

  for i in range(0,dimension):
    if currentNode.value == element:
      position = i
      break
    currentNode = currentNode.nextNode
  return position    
"""

#INSERT #Complejidad: O(n)
def insert(L,element,position):
  currentNode = L.head
  dimension = length(L)

  if position < 0 or position > dimension:
    position = None
  else:
    for i in range(0,position-1):
      currentNode = currentNode.nextNode

    new_node = Node()
    new_node.value = element
    new_node.nextNode = currentNode.nextNode
    currentNode.nextNode = new_node

  return position

#DELETE #Complejidad: O(n)
def delete(L,element):
  position = search(L,element)

  if position != None:
    dimension = length(L)
    currentNode = L.head

    if position == 0 :
      L.head = currentNode.nextNode

    for i in range(0,position-1):
      currentNode = currentNode.nextNode

    currentNode.nextNode = currentNode.nextNode.nextNode
    
  return position

#LENGTH #Complejidad: O(n)
def length(L):
  currentNode = L.head
  dimension = 0

  while currentNode != None:
    dimension = dimension + 1
    currentNode = currentNode.nextNode

  return dimension  


#ACCESS #Complejidad: O(n)
def access(L,position) :
  currentNode = L.head
  dimension = length(L)
  i = 0

  if position >= dimension or position < 0 :
    element = None
  else :
    for i in range(0,dimension):
      if i == position :
        element = currentNode.value
        break
      currentNode = currentNode.nextNode
  return element   

#UPDATE #Complejidad: O(n)
def update(L,element,position) :  
  current_element = access(L,position)
  dimension = length(L)
  currentNode = L.head
  
  if current_element != None:
    for i in range(0,dimension) :
      if currentNode.value == current_element :
        currentNode.value = element
        break
      currentNode = currentNode.nextNode 
  else :
    position = None    

  return position

#PRINTLIST
def print_list(L):
  print("")
  currentNode = L.head
  contador = 0
  print("--------------------------------")
  print("LinkedList:")
  print(end ="{")
  while currentNode != None :
   
    if currentNode.nextNode != None:
      print(currentNode.value, end=";")
    else:
      print(currentNode.value, end = "}")

    currentNode = currentNode.nextNode
  print("")  
  print("--------------------------------")  

##############EXTRAS##############

#MOVE
def move(L,position_orig,position_dest):
  #busca el value que se encuentra en la posicion de origen
  value_orig = access(L,position_orig)
  #busca el value que se encuentra en la posicion de destino
  value_dest = access(L,position_dest)
  #actualiza la lista ingresando el value de la posicion de origen en la posicion de destino
  update(L,value_orig,position_dest)
  #actualiza la lista ingresando el value de la posicion de destino en la posicion de origen
  update(L,value_dest,position_orig)

#ACCESS NODE
def accessNode(L,position):
	i = 0
	Node = None
	currentNode = L.head
	while (currentNode != None):
		if (i == position):
			Node = currentNode
			break
		i = i + 1
		currentNode = currentNode.nextNode
	return Node 


def delete_position(l,position): 
  currentNode = l.head
  n = 0
  if (l.head == None):
    return None
  elif (position == 0):
    l.head = l.head.nextNode
  else:
    while currentNode != None:
      if (n == position - 1):
        break
      n = n + 1
      currentNode = currentNode.nextNode
    currentNode.nextNode = currentNode.nextNode.nextNode

#Funcion que convierte una lista en vector
def toVector(l):
	tam = length(l)
	newArray = Array(tam,0)
	currentNode = l.head
	n = 0
	while currentNode != None:
		newArray[n] = currentNode.value
		n = n + 1
		currentNode = currentNode.nextNode
	return newArray

#Funcion que convierte un vector en una lista
def toList(v):
	tam = len(v)
	newList = LinkedList()
	n = tam - 1
	add(newList,v[n])
	n = n - 1
	while n >= 0:
		add(newList,v[n])
		n = n - 1
	return newList

def isSubL(L,S):

  #Inicializo variables
  currentNodeL = L.head
  currentNodeS = S.head
  i = 0  #contara la cantidad de elementos de S que se encuentran en L de manera consecutiva

  #este bucle recorre la lista L
  while currentNodeL != None :
    
    #analiza si currentNodeS es distinto de None, ya que si es None significa que no hay mas elementos en la lista

    if currentNodeS != None :
      #analiza si el elemento de la lista S esta en la lista L
      if currentNodeL.value == currentNodeS.value :
        #si se encuentra en la lista se incrementa el contador y tambien se recorre la lista S al siguiente nodo ya que todos los elementos de S se deben encontrar en L de manera consecutiva
        i = i + 1
        currentNodeS = currentNodeS.nextNode
      else : 
        #si el elemento no se encuentra en la lista se reinicia el recorrido en S para que se busque nuevamente si la S esta incluida en L 
        currentNodeS = S.head
        #se reinicia el contador ya que se empieza la busqueda nuevamente
        i = 0
       
    else :
      #de esta manera rompe el bucle ya que no hay mas elementos por analizar
      break
    currentNodeL = currentNodeL.nextNode  

  #compruebo si S se encuentra en L
  if i == length(S) :
    inclusion = True
    print("S ESTA INCLUIDA EN L")
  else :
    inclusion = False    
    print("S NO ESTA INCLUIDA EN L")

  return  inclusion  


