from algo1 import*
from linkedlist import *
from queue import *

class PriorityQueue:
  head=None

class PriorityNode:
  value=None
  nextNode=None
  priority=None

#PRIORITY ENQUEUE #Complejidad: O(n) #prioridad minima: 0
def enqueue_priority(Q,element,priority):
  dimension = length(Q)
  current_priority = priority
  position = 0

  if dimension != 0:
    new_prioritynode = PriorityNode()
    new_prioritynode.value = element  
    new_prioritynode.priority = priority

    #analizo la prioridad el primer elemento
    if Q.head.priority >= current_priority : #si es menor que la del primer elemento, colocamos el nuevo primer elemento
      new_prioritynode.nextNode = Q.head
      Q.head = new_prioritynode
    else:  
      currentNode = Q.head
      #recorro la cola mientras exista el elemento siguiente al actual
      while currentNode.nextNode != None:
        if current_priority < currentNode.priority:
          break
        elif current_priority == currentNode.priority:
          break 
        else:
          position = position + 1
          currentNode = currentNode.nextNode

      new_prioritynode.nextNode = currentNode.nextNode
      currentNode.nextNode = new_prioritynode      
  else:
    new_prioritynode = PriorityNode()
    new_prioritynode.value = element  
    new_prioritynode.priority = priority
    new_prioritynode.nextNode = Q.head
    Q.head = new_prioritynode
    
  return position
  
#PRIORITY DEQUEUE #Complejidad: O(n)
def dequeue_priority(Q):
  element = dequeue(Q)
  return element