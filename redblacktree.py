from algo1 import *
from avltree import *

class RedBlackTree:
  root = None

class RedBlackNode:
  parent = None
  leftnode = None
  rightnode = None
  key = None
  value = None
  color = None

#INSERT
def RBFixup(T, z):

  while z.parent != None and z.parent.color == True:

    if z.parent == z.parent.parent.leftnode:
      y = z.parent.parent.rightnode

      if y.color == True:

        z.parent.color = False
        y.color = False
        z.parent.parent.color = True
        z = z.parent.parent
      else:

        if z == z.parent.rightnode:
          z = z.parent
          rotateLeft(T, z)

        z.parent.color = False
        z.parent.parent.color = True
        rotateRight(T, z.parent.parent)

    else:
      y = z.parent.parent.leftnode
        
      if y.color == True:

        z.parent.color = False
        y.color = False
        z.parent.parent.color = True
        z = z.parent.parent
      else:

        if z == z.parent.leftnode:
          z = z.parent
          rotateRight(T, z)
            
        z.parent.color = False
        z.parent.parent.color = True
        rotateLeft(T, z.parent.parent)
  
  T.root.color = False  

def insertRBTR(T, z):
  x = T.root

  while x != None:
    y = x

    if z.key < x.key:
      x = x.leftnode
    else:
      x = x.rightnode
  
  z.parent = y

  if y == None:
    T.root = z
  elif z.key < y.key:
    y.leftnode = z
  else:
    y.rightnode = z
  
  z.color = True

  RBFixup(T, z)

def insertRBT(RBT, element, key):
  newNode = RedBlackNode()
  newNode.key = key
  newNode.value = element
  #caso en el que el arbol este vacio y se deba añadir la raiz
  if RBT.root == None:
    RBT.root = newNode
    RBT.root.color = False
    return newNode.key
  else:
    result = insertRBTR(RBT, newNode)

    return result

#DELETE

def transplant(T, oldn, newn):
  
  if oldn.parent == None: #si el parent del nodo viejo es none, entonces el nuevo nodo sera la raiz
    T.root == newn
  else:
    if oldn == oldn.parent.leftnode: #si el nodo viejo era el nodo izquierdo, este sera el nuevo nodo
      oldn.parent.leftnode = newn
    else: #sino, será el derecho
      oldn.parent.rightnode = newn
    
  if newn != None: #si el nuevo nodo es distinto a None, el padre de este sera el padre del nodo viejo
    newn.parent = oldn.parent

def delete_fixup(T, x):

  while x != T.root and x.color == False:
    if x == x.parent.leftnode:
      w = x.parent.rightnode

      if w.color == True:
        w.color = False
        x.parent.color = True
        rotateLeft(T, x.parent)
        w = x.parent.rightnode
      
      if w.leftnode.color == False and w.rightnode.color == False:
        w.color = True
        x = x.parent
      
      else:

        if w.rightnode.color == False:
          w.leftnode.color = False
          w.color = True
          rotateRight(T, w)
          w = x.parent.rightnode
        
        w.color = x.parent.color
        x.parent.color = False
        w.rightnode.color = False
        rotateLeft(T, x.parent)
        x = T.root
    
    elif x == x.parent.rightnode:
      w = x.parent.leftnode

      if w.color == True:
        w.color = False
        x.parent.color = True
        rotateRight(T, x.parent)
        w = x.parent.leftnode
      
      if w.rightnode.color == False and w.leftnode.color == False:
        w.color = True
        x = x.parent
      
      else:

        if w.leftnode.color == False:
          w.rightnode.color = False
          w.color = True
          rotateLeft(T, w)
          w = x.parent.leftnode
        
        w.color = x.parent.color
        x.parent.color = False
        w.leftnode.color = False
        rotateRight(T, x.parent)
        x = T.root
  
  x.color = False

def minimum(z): #devuelve el nodo más pequeño del árbol o subárbol
  if z.leftnode != None:
    z = z.leftnode
  else:
    return z


def deleteRBT(T, z):
  y = z
  y_orig_color = y.color #guardamos color del nodo a borrar

  if z.leftnode == None: #si z no tiene leftnode, el ndoo a borrar se vuelve el derecho
    x = z.rightnode
    transplant(T, z, z.rightnode)

  elif z.rightnode == None: #si z no tiene leftnode, el nodo a borrar es el izquierdo
    x = z.leftnode
    transplant(T, z, z.leftnode)
  
  else: #si z tiene ambos hijos, usamos al sucesor de z
    y = minimum(z.rightnode)
    y_orig_color = y.color
    x = y.rightnode
  
    if y.parent == z: #si z es el hijo de y, el padre de la rama derecha de y sera y
      x.parent = y
    
    else: #si no es hijo de y, el hijo derecho es y
      transplant(T, y, y.rightnode)
      y.rightnode = z.rightnode
      y.rightnode.parent = y
    
    transplant(T, z, y)
    y.leftnode = z.leftnode
    y.leftnode.parent = y
    y.color = z.color
  
  if y_orig_color == False:
    delete_fixup(T,x)
