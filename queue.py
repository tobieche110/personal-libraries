from algo1 import*
from linkedlist import*

#ENQUEUE #Complejidad: O(1)
def enqueue(Q,element):
  add(Q,element)

#DEQUEUE #Complejidad: O(n)
def dequeue(Q):
  dimension = length(Q)
  element = access(Q,dimension-1)

  if element != None:
    delete(Q,element)
  
  return element
  