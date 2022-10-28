from algo1 import*
from linkedlist import*
from binarytree import*
from queue import*

class AVLTree:
  root = None

class AVLNode:
  key = None
  value = None
  leftnode = None
  rightnode = None
  parent = None
  balancefactor = None
  height = None

#INSERT R
def insertAVLR(newNode,currentNode):
  key = newNode.key
  #analiza si la key ingresada es menor que la del nodo
  if newNode.key < currentNode.key :
    if currentNode.leftnode == None:
      currentNode.leftnode = newNode
      newNode.parent = currentNode
    else:
      insertAVLR(newNode,currentNode.leftnode)
  #analiza si la key ingresada es mayor que la del nodo  
  elif  newNode.key > currentNode.key :  
    if currentNode.rightnode == None:
      currentNode.rightnode = newNode
      newNode.parent = currentNode
    else:
      insertAVLR(newNode,currentNode.rightnode)
  else: #al no ser ni mayor ni menor significa que es igual, por lo tanto el valor ya ha sido ingresado. De esta manera el elemento no se ingresa y devuelve None
    print("Error: ya existe un nodo con la key ingresada.")
    key = None
  return key

def insertAVL(B,element,key):
  newNode = AVLNode()
  newNode.key = key
  newNode.value = element
  #caso en el que el arbol este vacio y se deba añadir la raiz
  if B.root == None:
    B.root = newNode
    return newNode.key
  else:
    result = insertAVLR(newNode,B.root)
    
    rebalance(B)
    return result

#CALCULAR ALTURA DESDE NODO DE ARBOL
def treeHeightR(node):
  if node == None:
    return 0
  else:
    return 1 + max(treeHeightR(node.rightnode), treeHeightR(node.leftnode))

def treeHeight(node):
    h = treeHeightR(node)

    return h - 1

#ROTATE
def rotateRight(Tree, avlnode):

  newRoot = avlnode.leftnode
  avlnode.leftnode = newRoot.rightnode

  if newRoot.rightnode != None:
    newRoot.rightnode.parent = avlnode
  newRoot.parent = avlnode.parent

  if avlnode.parent == None:
    Tree.root = newRoot
  else:
    if avlnode.parent.rightnode == avlnode:
      avlnode.parent.rightnode = newRoot
    else:
      avlnode.parent.leftnode = newRoot
  
  newRoot.rightnode = avlnode
  avlnode.parent = newRoot

  return newRoot

def rotateLeft(Tree, avlnode):
  
  newRoot = avlnode.rightnode
  avlnode.rightnode = newRoot.leftnode

  if newRoot.leftnode != None:
    newRoot.leftnode.parent = avlnode
  newRoot.parent = avlnode.parent

  if avlnode.parent == None:
    Tree.root = newRoot
  else:
    if avlnode.parent.leftnode == avlnode:
      avlnode.parent.leftnode = newRoot
    else:
      avlnode.parent.rightnode = newRoot
  
  newRoot.leftnode = avlnode
  avlnode.parent = newRoot

  return newRoot

#CALCULATE BALANCE
def calculateBalanceR(node): 

  if node.rightnode != None:
    calculateBalanceR(node.rightnode)

  if node.leftnode != None:
    calculateBalanceR(node.leftnode)

  node.balancefactor = treeHeight(node.leftnode) - treeHeight(node.rightnode)
  node.height = treeHeight(node)

def calculateBalance(AVLTree):
  if AVLTree.root == None:
    print("Arbol vacio")
    return None
  else:
    calculateBalanceR(AVLTree.root)
    return AVLTree

#REBALANCE
def rebalanceR(AVLTree, node):

  if node.balancefactor >= 2:

    if node.leftnode.balancefactor == -1:
      rotateLeft(AVLTree,node.leftnode)
      rotateRight(AVLTree,node)  
    else:  
      rotateRight(AVLTree,node)  

  elif node.balancefactor <= -2 :
    
    if node.rightnode.balancefactor == 1:
      rotateRight(AVLTree,node.rightnode)
      rotateLeft(AVLTree,node)
    else:
      rotateLeft(AVLTree,node)

def rebalance(AVLTree):
  if AVLTree.root == None:
    print("Arbol vacío")
    return None
  else:
    calculateBalance(AVLTree)
    rebalanceR(AVLTree, AVLTree.root)

    return AVLTree
    
#DELETE
def deleteNodeAVL(B): #Debemos eliminar la raiz del arbol y promover los demas
  raiz = B.root 
  # El nodo que queremos eliminar tiene 2 hijos
  if(raiz.leftnode != None and raiz.rightnode != None):
    arbol_derecho = AVLTree()
    arbol_derecho.root = raiz.rightnode 
    menor = getMenorBT(arbol_derecho) # Obtenemos el menor de los mayores
    print("ASCENSO: " + str(menor.value))
    
    raiz.key = menor.key
    raiz.value = menor.value
    
    arbol = AVLTree()
    arbol.root = menor
    deleteNodeAVL(arbol)
  #El nodo tiene un solo hijo izquierdo
  elif(raiz.leftnode != None):
    reemplazar(raiz,raiz.leftnode)
  #El nodo tiene un solo hijo derecho
  elif(raiz.rightnode != None):
    reemplazar(raiz,raiz.rightnode)
  #El nodo es una hoja
  else:
    reemplazar(raiz,None)
    
def deleteAVL(B,element): 
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
      rama_izq = AVLTree()
      rama_izq.root = raiz.leftnode
      deleteAVL(rama_izq,element)
    # Si el elemento está por la derecha, formamos un arbol con la rama derecha y lo buscamos ahi
    elif(busqueda > raiz.key):
      rama_der = AVLTree()
      rama_der.root = raiz.rightnode
      deleteAVL(rama_der, element)
    #Encontramos el nodo que queremos eliminar
    else: 
      retorno = raiz.key
      arbol = AVLTree()
      arbol.root = raiz
      deleteNodeAVL(arbol) # Llamamos a deleteNode y pasamos el arbol donde se debe eliminar la raiz
  else:
    retorno = None
  rebalance(B)
  return retorno

