import ctypes
class DynamicArray:
  def __init__(self):
    self.n = 0 # number of elements
    self.capacity = 1 # default capacity is 1
    self.A = self.make_array(self.capacity)

  def __len__(self):
    """
    Return number of elements stored in Array

    """
    return self.n

  def get(self,k):
    """
    Return element at index k

    """
    if not 0<=k<self.n:
      # Check if k is within bounds of array, if not raise index error
      raise IndexError
    # return element at index k
    return self.A[k]

  def set(self,idx,item):
    """
    This function assigns a value to the array, useful for sorting algorithms
    """
    if not 0<=idx<self.n:
      raise IndexError
    self.A[idx] = item 

  def search_by_id(self,target_id):
    """
    This function searches an event by id
    """
    for i in range(len(self)):
      if self.get(i).id == target_id:
        return 'Event found'
    return 'Event not found'


  def append(self, ele):
    """
    This function insert element at the end of the array
    """
    if self.n == self.capacity:
      # Double capacity if not enough space
      self._resize(2*self.capacity)
    self.A[self.n] = ele
    self.n+=1

  def insert(self,item,idx):
    """
    This function insert element at any specific index
    """
    if idx < 0 or idx > self.n:
      raise IndexError
    if self.n == self.capacity:
      self._resize(2*self.capacity)
    for i in range(self.n-1,idx-1,-1):
      self.A[i+1] = self.A[i]
    self.A[idx] = item
    self.n+=1

  def delete(self):
    """
    This function deletes element from end of array
    """
    if self.n==0:
      print('Array is already empty, deletion is not possible')
      return
    temp = self.A[self.n-1]
    self.A[self.n-1]=0
    self.n-=1
    return temp

  def remove(self,idx):
    """
    This function removes element from the specific index of an array
    """
    temp = self.A[idx]
    if self.n==0:
      print('Array is alreay is empty, deletion is not possible')
    if idx < 0 or idx >= self.n:
      raise IndexError
    if idx == self.n-1:
      self.A[idx]=0
      self.n-=1
      return temp
    for i in range(idx, self.n-1):
      self.A[i]=self.A[i+1]
    self.A[self.n-1]=0
    self.n-=1
    return temp

  def _resize(self, new_cap):
    """
    Resize internal array to capacity new_cap
    """
    B = self.make_array(new_cap) # New bigger array
    for k in range(self.n):
      B[k] = self.A[k] # reference all existing elements
    self.A = B # Call A the new big Array
    self.capacity = new_cap

  def make_array(self,new_cap):
    """
    Returns a new array with new_cap capacity
    """
    return (new_cap * ctypes.py_object)()

  def list_all(self):
        return [self.A[i] for i in range(self.n)]