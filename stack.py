from algo1 import*
from linkedlist import*

#PUSH #Complejidad: O(1)
def push(S,element):
  add(S,element)

#POP #Complejidad: O(n)
def pop(S):
  element = access(S,0)

  if element != None :
    delete(S,element)

  return element  