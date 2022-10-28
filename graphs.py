from algo1 import*
from linkedlist import*

def printGraph(G): #Función que imprime los valores que hay en cada lista de adyacencia
  for i in range(0, len(G)):
    print("CONNECTED TO ",G[i].head.value)
    currentNode = G[i].head.nextNode
    while currentNode != None:
      print(currentNode.value)
      currentNode = currentNode.nextNode
    print("")

#EJERCICIO 1
def addLast(L, element):
  currentNode = L.head
  while currentNode.nextNode != None:
    currentNode = currentNode.nextNode
  
  newNode = Node()
  newNode.value = element
  currentNode.nextNode = newNode

def searchVertPos(graph, element):
  for i in range(0, len(graph)):
    if graph[i].head.value == element:
      return i
  
  return None

def createGraph(vertices, aristas):

  graph = Array(length(vertices), LinkedList())

  currentNode = vertices.head
  for i in range(0, len(graph)):
    graph[i] = LinkedList()
    add(graph[i], currentNode.value)
    currentNode = currentNode.nextNode

  currentNode = aristas.head
  for i in range(0, length(aristas)):
    addLast(graph[searchVertPos(graph, int(currentNode.value[0]))], int(currentNode.value[2]))
    addLast(graph[searchVertPos(graph, int(currentNode.value[2]))], int(currentNode.value[0]))
    currentNode = currentNode.nextNode

  return graph

#EJERCICIO 2
def existPath(graph, v1, v2):
  listPosition = searchVertPos(graph, v1)

  if search(graph[listPosition], v2) != None:
    return True
  
  return False

#EJERCICIO 3
def isConnected(graph):
  #se busca el recorrido = len(graph) que pase por todos los vertices
  lenGraph = len(graph)
  tracedVertex = Array(lenGraph, 0)
  route = 0

  for i in range(0, lenGraph):

    currentNode = graph[i].head
    while currentNode != None:

      for j in range(0, lenGraph):

        if tracedVertex[j] == currentNode.value:
          break
        elif j == lenGraph - 1 and currentNode.value != graph[i].head.value:
          tracedVertex[route] = currentNode.value
          route = route + 1
          

      currentNode = currentNode.nextNode

  if route == lenGraph:
    return True
  else:
    return False

#EJERCICIO 4
def compareLists(list1, list2):
  currentNode1 = list1.head
  headValue1 = list1.head.value
  headValue2 = list2.head.value

  if list1 != list2:
    while currentNode1 != None:
      currentNode2 = list2.head

      while currentNode2 != None:
        if currentNode1.value == currentNode2.value and headValue1 != currentNode2.value and headValue2 != currentNode2.value:
          return False
        currentNode2 = currentNode2.nextNode

      currentNode1 = currentNode1.nextNode
    
    return True

def isTree(graph):
  #para que sea árbol, el nodo2 apuntado por el nodo1 no debe apuntar a un nodo que apunte el nodo1

  for i in range(0, len(graph)):
    list1 = graph[i]
    currentNode = list1.head

    while currentNode != None:
      if compareLists(list1, graph[searchVertPos(graph, currentNode.value)]) == False:
        return False
      currentNode = currentNode.nextNode

  if isConnected(graph) == True:
    return True

#EJERCICIO 7
def countConnections(graph):
  connections = 0
  for i in range(0, len(graph)):
    currentNode = graph[i].head.nextNode
    while currentNode != None:
      connections = connections + 1
      currentNode = currentNode.nextNode

  return connections/2

#EJERCICIO 8
def deleteRepeated(list1, list2):
  currentNode1 = list1.head
  headValue1 = list1.head.value
  headValue2 = list2.head.value

  if list1 != list2:
    while currentNode1 != None:
      currentNode2 = list2.head

      while currentNode2 != None:
        if currentNode1.value == currentNode2.value and headValue1 != currentNode2.value and headValue2 != currentNode2.value:
          delete(list2, currentNode2.value)
        currentNode2 = currentNode2.nextNode

      currentNode1 = currentNode1.nextNode
    
    return True 

def convertToTree(graph):
  #igual que isTree pero eliminamos aquellos nodos que se repitan.

  for i in range(0, len(graph)):
    list1 = graph[i]
    currentNode = list1.head

    while currentNode != None:
      deleteRepeated(list1, graph[searchVertPos(graph, currentNode.value)])
      currentNode = currentNode.nextNode

  return graph

#EJERCICIO 13
def listToMatrix(graph): #funcion que desde una lista de adyacencia, la convierte en matriz
  lenGraph = len(graph) + 1
  matrix = Array(lenGraph, Array(lenGraph, 0))

  for i in range(0, lenGraph):
    for j in range(0, lenGraph):
      matrix[i][j] = 0
  
  for i in range(0, lenGraph - 1):
    currentNode = graph[i].head.nextNode
    column = searchVertPos(graph, graph[i].head.value) + 1
    while currentNode != None:
      line = searchVertPos(graph, currentNode.value) + 1
      matrix[column][line] = 1
      currentNode = currentNode.nextNode
  
  for i in range(0, lenGraph - 1):
    for j in range(0, lenGraph - 1):
      if i == 0:
        matrix[i][j + 1] = graph[j].head.value
      if j == 0:
        matrix[i + 1][j] = graph[i].head.value
  
  return matrix

def convertToTreeM(matrix): #funcion que desde matriz de adyacencia, convierte en arbol

  lenM = len(matrix)

  for i in range(0, lenM):
    for j in range(0, lenM):

      if matrix[i][j] == 1 and i != 0 and j != 0:

        for k in range(0, lenM):
          if matrix[i][k] == 1 and matrix[j][k] == 1:
            matrix[j][k] = 0
        
  return matrix