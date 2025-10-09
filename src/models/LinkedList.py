class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:

  def __init__(self):

    self.head=None
    self.length = 0

  def __len__(self):
    return self.length

  def __str__(self):
    elements = []
    current = self.head
    to_print =""
    while current:
      to_print+=f"{current.value} -> "
      current = current.next
    return to_print


  def push(self,data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node


  def append(self,data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      current = self.head
      while current.next:
        current = current.next
      current.next = new_node
    self.length+=1


  def getAt(self,index):
    current = self.head
    for i in range(index):
      current = current.next
    return current.value

  def insertAt(self,index, value):
    if not 0 <= index <= self.length:
      raise IndexError(f"index is out of range")

    if index==0:
      self.push(value)
      return

    elif index == self.length:
      self.append(value)
      return

    new_node = Node(value)
    current = self.head
    for i in range(index-1):
      current = current.next
    new_node.next = current.next
    current.next = new_node
    self.length+=1

  def removeAt(self, index):
    if not 0 <= index <= self.length:
      raise IndexError(f"index is out of range")

    if index == 0:
      self.head = self.head.next

    else:
      current = self.head
      for i in range(index-1):
        current = current.next
      current.next = current.next.next
    self.length-=1
