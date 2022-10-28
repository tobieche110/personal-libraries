from algo1 import*
from linkedlist import*
from queue import*

class BinaryTree:
  root = None

class BinaryTreeNode:
  key = None
  value = None
  leftnode = None
  rightnode = None
  parent = None

#SEARCH R
def searchBTR(element,currentNode):
  #analiza si encontro el elemento
  if currentNode.value == element:
    key = currentNode.key
  else:
    key = None
    #si existe un nodo izquierdo sigue la busqueda por alli
    if currentNode.leftnode != None :
      key = searchBTR(element,currentNode.leftnode)    
    #si no se encontro el elemento, busca por el nodo derecho
    if key == None and currentNode.rightnode != None:
      key = searchBTR(element,currentNode.rightnode)    

  return key  

#SEARCH #Complejidad: -promedio: O(log n) -peor: O(n)
def searchBT(B,element):
  #analiza si el arbol esta vacio
  if B.root == None:
    print("Arbol vacio")
    return None
  else:
    key = searchBTR(element,B.root)  
    return key

#INSERT R
def insertBTR(newNode,currentNode):
  key = newNode.key
  #analiza si la key ingresada es menor que la del nodo
  if newNode.key < currentNode.key :
    if currentNode.leftnode == None:
      currentNode.leftnode = newNode
      newNode.parent = currentNode
    else:
      insertBTR(newNode,currentNode.leftnode)
  #analiza si la key ingresada es mayor que la del nodo  
  elif  newNode.key > currentNode.key :  
    if currentNode.rightnode == None:
      currentNode.rightnode = newNode
      newNode.parent = currentNode
    else:
      insertBTR(newNode,currentNode.rightnode)
  else: #al no ser ni mayor ni menor significa que es igual, por lo tanto el valor ya ha sido ingresado. De esta manera el elemento no se ingresa y devuelve None
    print("Error: ya existe un nodo con la key ingresada.")
    key = None
  return key  

#INSERT #Complejidad: -promedio: O(log n) -peor: O(n)
def insertBT(B,element,key):
  newNode = BinaryTreeNode()
  newNode.key = key
  newNode.value = element
  #caso en el que el arbol este vacio y se deba añadir la raiz
  if B.root == None:
    B.root = newNode
    return newNode.key
  else:
    result = insertBTR(newNode,B.root)
    return result

#REEMPLAZAR   
def reemplazar(raiz,nodo):
  #Al padre asignamos el nuevo hijo
  if(raiz.parent != None):
    padre = raiz.parent
    #Comprobamos si es nodo derecho
    if(padre.rightnode != None and raiz.value == padre.rightnode.value): 
      padre.rightnode = nodo
    #Comprobamos si es nodo izquierdo
    elif(padre.leftnode != None and raiz.value == padre.leftnode.value):
      padre.leftnode = nodo
  #Al nuevo padre asignamos su hijo
  if(nodo != None):
    nodo.parent = raiz.parent

  

#Buscamos el menor de sus mayores
def getMenorBT(B): 
  raiz = B.root
  while(raiz.leftnode != None):
    raiz = raiz.leftnode
  return raiz


def deleteNodeBT(B): #Debemos eliminar la raiz del arbol y promover los demas
  raiz = B.root 
  # El nodo que queremos eliminar tiene 2 hijos
  if(raiz.leftnode != None and raiz.rightnode != None):
    arbol_derecho = BinaryTree()
    arbol_derecho.root = raiz.rightnode 
    menor = getMenorBT(arbol_derecho) # Obtenemos el menor de los mayores
    print("ASCENSO: " + str(menor.value))
    
    raiz.key = menor.key
    raiz.value = menor.value
    
    arbol = BinaryTree()
    arbol.root = menor
    deleteNodeBT(arbol)
  #El nodo tiene un solo hijo izquierdo
  elif(raiz.leftnode != None):
    reemplazar(raiz,raiz.leftnode)
  #El nodo tiene un solo hijo derecho
  elif(raiz.rightnode != None):
    reemplazar(raiz,raiz.rightnode)
  #El nodo es una hoja
  else:
    reemplazar(raiz,None)
    
#DELETE
def deleteBT(B,element): 
  global retorno
  busqueda = searchBT(B,element)
  if(busqueda != None):
    raiz = B.root
    # Si el arbol está vacio retornamos None
    if(busqueda == None):
      print("Nodo no encontrado")
      retorno = None
    # Si el elemento está por la izquierda, formamos un arbol con la rama izquierda y lo buscamos ahi
    elif(busqueda < raiz.key):
      rama_izq = BinaryTree()
      rama_izq.root = raiz.leftnode
      deleteBT(rama_izq,element)
    # Si el elemento está por la derecha, formamos un arbol con la rama derecha y lo buscamos ahi
    elif(busqueda > raiz.key):
      rama_der = BinaryTree()
      rama_der.root = raiz.rightnode
      deleteBT(rama_der, element)
    #Encontramos el nodo que queremos eliminar
    else: 
      print("Elemento: " + str(raiz.value) + " KEY: " + str(raiz.key))
      retorno = raiz.key
      arbol = BinaryTree()
      arbol.root = raiz
      deleteNodeBT(arbol) # Llamamos a deleteNode y pasamos el arbol donde se debe eliminar la raiz
  else:
    retorno = None
  return retorno

#DELETE KEY
def deleteKey(B,key): 
  #analiza si es un arbol vacio
  if B.root == None :
    return None
  else :
    #analiza si la key ingresada se encuentra en el arbol 
    element = access(B,key)

    return deleteBT(B,element)

#ACCESS R
def accessBTR(key,currentNode):
 
  #asigna el valor de nodo a la variable cuando se encontro el nodo
  if currentNode.key == key:
    element = currentNode.value
  else:
    element = None
    #si el elemento es mayor que currentNode se dirige al subarbol derecho
    if key < currentNode.key:
      if currentNode.leftnode != None:
        #invoca a la funcion recursiva con nuevos parametros
        element = accessBTR(key,currentNode.leftnode)  
    # si el elemento es menor que currentNode se dirige al subarbol izquierdo
    if element== None and key > currentNode.key:
      if currentNode.rightnode != None:
        #invoca a la funcion recursiva con nuevos parametros
        element = accessBTR(key,currentNode.rightnode)

  return element
  
#ACCESS #Complejidad: -promedio: O(log n) -peor: O(n)
def accessBT(B,key):

  if B.root == None:
    print("Arbol vacio")
    return None  
  else:
    element = accessBTR(key,B.root)
    return element

#UPDATE R
def updateBTR(element,key,currentNode):

  #asigna el valor a key en caso de haber encontrado el elemento
  if key == currentNode.key :
    currentNode.value = element
  else :  
    #si el elemento es mayor que currentNode se dirige al subarbol derecho
    if key > currentNode.key :

      if currentNode.rightnode != None : 
        #invoca a la funcion recursiva con nuevos parametros
        key = updateBTR(element,key,currentNode.rightnode)
    else : # si el elemento es menor que currentNode se dirige al subarbol izquierdo

      if currentNode.leftnode != None : 
        #invoca a la funcion recursiva con nuevos parametros
        key = updateBTR(element,key,currentNode.leftnode)
  return key

#UPDATE #Complejidad
def updateBT(B,element,key):

  if B.root == None:
    print("Arbol vacio")
    return None
  elif accessBT(B,key) == None:  
    return None
  else:
    key = updateBTR(element,key,B.root)       
    return key  

##############EXTRAS##############

#SEARCH NODE R
def searchBTnodeR(element,currentNode):
  #verifica si el elemento se encuentra en currentNode 
  if currentNode.value == element:
    node = currentNode
  else:
    node = None
    #busca por un subarbol izquierdo
    if currentNode.leftnode != None:
      node = searchBTnodeR(element,currentNode.leftnode)
    #busca por un subarbol derecho
    if node == None and currentNode.rightnode != None:
      node = searchBTnodeR(element,currentNode.rightnode)  

  return node

#SEARCH NODE
def searchBTnode(B,element):
  #analiza si el arbol esta vacio
  if B.root == None:
    print("Arbol vacio")
    return None
  else:
    node = searchBTnodeR(element,B.root)  

#ACCESS NODE R
def accessBTnodeR(key,currentNode):
  #analiza si encontro el nodo con la key buscada y le asigna el puntero a la variable
  if currentNode.key == key:
    node = currentNode
  else:
    node = None
    #si la key es menor se dirige al subarbol izquierdo
    if key < currentNode.key:
      #analiza si existe un nodo izquierdo
      if currentNode.leftnode != None:
        node = accessBTnodeR(key,currentNode.leftnode)

    #si la key es mayor se dirige al subarbol derecho
    if key > currentNode.key:
      #analiza si existe un nodo derecho
      if currentNode.rightnode != None:
        node = accessBTnodeR(key,currentNode.rightnode)

  return node       

#ACCESS NODE
def accessBTnode(B,key):
  #Analiza si el arbol esta vacio
  if B.root == None:
    print("Arbol vacio")
    return None
  else:
    node = accessBTnodeR(key,B.root)  
    return node
    

##############TRAVERSE##############
#TRAVERSE IN ORDER R
def traverseInOrderR(L,currentNode):
  #analiza si existe un nodo izquierdo
  if currentNode.leftnode != None:
    #llamado a la funcion recursiva
    traverseInOrderR(L,currentNode.leftnode)
  #  
  insert(L,currentNode.value,length(L))
  #analiza si existe un nodo derecho
  if currentNode.rightnode != None:
    #llamado a la funcion recursiva
    traverseInOrderR(L,currentNode.rightnode)  

#TRAVERSE IN ORDER
def traverseInOrder(B):
  #analiza si el arbol esta vacio
  if B.root == None:
    print("Arbol vacio")
    return None
  else:
    #creo lista enlazada
    L = LinkedList()  
    traverseInOrderR(L,B.root)
    return L

#TRAVERSE IN POST ORDER R
def traverseInPostOrderR(L,currentNode):
  
  #analiza si el nodo actual tiene hijos por izquierda
  if currentNode.leftnode != None:
    traverseInPostOrderR(L,currentNode.leftnode)
  #analiza si el nodo actual tiene hijos por derecha
  if currentNode.rightnode != None:
    traverseInPostOrderR(L,currentNode.rightnode)  
  #al llegar a esta instancia se insertan los nodos hoja de los subarboles, y luego las raices de estos nodos hoja  
  insert(L,currentNode.value,length(L))  

#TRAVERSE IN POST ORDER
def traverseInPostOrder(B):
  #analiza si el arbol esta vacio
  if B.root == None:
    print("Arbol vacio")
    return None
  else:
    #creo lista enlazada
    L = LinkedList()
    traverseInPostOrderR(L,B.root) 
    return L 

#TRAVERSE IN PRE ORDER R
def traverseInPreOrderR(L,currentNode):
  #
  insert(L,currentNode.value,length(L))
  #analiza si existe un nodo izquierdo
  if currentNode.leftnode != None:
    traverseInPreOrderR(L,currentNode.leftnode)
  #analiza si existe nodo derecha   
  if currentNode.rightnode != None:
    traverseInPreOrderR(L,currentNode.rightnode)  

#TRAVERSE IN PRE ORDER
def traverseInPreOrder(B):
  #analiza si el arbol esta vacio
  if B.root == None:
    print("Arbol vacio")
    return None
  else:
    #creo lista enlazada
    L = LinkedList()
    traverseInPreOrderR(L,B.root)  
    return L

#TRAVERSE BREADTH FIRST R
def traverseBreadthFirstR(L,Q,currentNode):
  #analiza si existe el nodo
  if currentNode != None:
    #analiza si existe un nodo izquierdo
    if currentNode.leftnode != None:
      insert(L,currentNode.leftnode.value,length(L))
      enqueue(Q,currentNode.leftnode)
      
    #analiza si existe un nodo derecho  
    if currentNode.rightnode != None:
      insert(L,currentNode.rightnode.value,length(L))
      enqueue(Q,currentNode.rightnode)
      
    traverseBreadthFirstR(L,Q,dequeue(Q))  

#TRAVERSE BREADTH FIRST
def traverseBreadthFirst(B):
  #analiza si el arbol esta vacio
  if B.root == None:
    print("Arbol vacio")
    return None
  else:
    #creo una lista enlazada y una cola
    L = LinkedList()
    Q = LinkedList() 
    add(L,B.root.value)
    traverseBreadthFirstR(L,Q,B.root)
    return L