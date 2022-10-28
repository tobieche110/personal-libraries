from algo1 import *
from linkedlist import*
from array import *

class dictionary:
  head = None

class dictionaryNode:
  value = None
  key = None
  nextNode = None

slotsSize = 9

#Imprime un diccionario con colisiones encadenadas
#El formato de los nodos es [k: key ;v: value]
def printD(D):
    n = len(D)
    for i in range(0,n):
        currentNode = D[i]
        if currentNode!=None:
            currentNode = D[i].head
            print("Slot",i,': ',end='')
            while currentNode!=None:
                if currentNode.nextNode!=None:
                        print("[k:",currentNode.key,";v:",currentNode.value,"] ➝ ",end="")
                else:
                    print("[k:",currentNode.key,";v:",currentNode.value,"] ➝ ",currentNode.nextNode,"\n") 
                currentNode = currentNode.nextNode
        else:
            print("Slot",i,": ",currentNode,"\n")


#PUNTO 1
def hash(key):
 return key%slotsSize

#def hash(c):
 # return ord(c)-ord('a')

#INSERT
def addDictionary(D, element, key):
  newNode = dictionaryNode()
  newNode.value = element
  newNode.key = key
  newNode.nextNode = D.head
  D.head = newNode

def insertHash(D, key, value):
  slot = hash(key)

  if D[slot] == None:
    L = dictionary()
    addDictionary(L, value, key)
    D[slot] = L
  else:
    addDictionary(D[slot], value, key)
  
  return D

#SEARCH
def searchHash(D, key):
  
  slot = hash(key)

  if D[slot] != None:
    currentNode = D[slot].head

    while currentNode != None:
      if currentNode.key == key:
        return key
      currentNode = currentNode.nextNode
  
  return None

#DELETE
def deleteHash(D, key):

  slot = hash(key)

  currentNode = D[slot].head

  while currentNode != None:
    if currentNode.key == key:
      currentNode.key = None
      return currentNode.value
    currentNode = currentNode.nextNode
  
  return None

#EJERCICIO 4; O(n)
def isPermutation(s, p):
  lenS = len(s)
  lenP = len(p)

  if lenS == lenP:
    ordS = 0
    ordP = 0
    for i in range(0, lenS):
      ordS = ordS + ord(s[i])
      ordP = ordP + ord(p[i])
    
    if ordP == ordS:
      return True
  
  return False

#EJERCICIO 5
def insertUnique(D, key, value):
    slot = hash(key)

    if(D[slot] == None):
        L = dictionary()
        D[slot] = L
        addDictionary(L,value,key)
    else:
        if(searchHash(D, key) != None):
            return False
        else:
            addDictionary(D[slot],value,key)

    return True

def isUnique(L):
    #aplicamos la hash function a la key ingresada por parametro, de esta manera obtenemos el slot donde se almacenara 
    m = 29# TAMAÑO DE SLOTS-- SE CAMBIA SEGUN NECESIDAD 
    D = Array(m,dictionary())
    dimensionL = len(L)

    for i in range(0,dimensionL):
        if(insertUnique(D,L[i],None) == False):
           return False

    return True

#EJERCICIO 6
def hashPostal(codigo):

  if len(codigo) == 8:
    total = 0

    for i in range(0, 8):
      total = total + ord(codigo[i])
    
    return hash(total - ord("A"))
  
  return None

#EJERCICIO 7

def compressor(s):
  dim = len(s)

  D = Array(slotsSize,dictionary())
  k = 1
  word = ""
  for i in range(0,dim):

    if searchHash(D,s[i]) != None:
      k = k + 1
    else: 
      insertHash(D,s[i],s[i])
      if k == 1:
        word = word + s[i]  
      else:
        deleteHash(D,s[i-1]) 
        word = word + str(k) + s[i] 
        k = 1

  if i == dim-1:
    if k != 1:          
      word = word+str(k)     
        
     
  return word

#Ejercicio 8 O(n)
def findSubString(s, p):

  dimS = len(s)
  dimP = len(p)

  k = 0 #contador de p #holaoli #oli

  for i in range(0, dimS):
    if s[i] == p[k]:
      k = k + 1
      if k == 1:
        firstPick = i
      if k == dimP:
        return firstPick
    else:
      k = 0
      firstPick = None

  return None

#Ejercicio 9: O(n^2)
def isSubSet(s, p):

  D = Array(9, dictionary())
  colisions = 0

  lenS = len(s)
  lenP = len(p)

  for i in range(0, lenS):
    insertHash(D, s[i], s[i])
  
  for i in range(0, lenP):
    if searchHash(D, p[i]) != None:
      colisions = colisions + 1

  if colisions == lenP:
    return True
  else:
    return False

