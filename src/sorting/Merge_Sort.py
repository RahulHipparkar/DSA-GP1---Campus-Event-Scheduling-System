# import sorting.Slicing
# import sorting.Get_Key 
from sorting.Get_Key import key
from sorting.Slicing import slice_array
from models.ArrayList import DynamicArray
def merge(a,b):
  n = a.__len__()
  m = b.__len__()
  result = DynamicArray()
  i = 0
  j = 0
  while i < n and j < m :
    if key(a.get(i)) < key(b.get(j)):
      result.append(a.get(i))
      i=i+1
    else:
      result.append(b.get(j))
      j=j+1
  while i < n:
    result.append(a.get(i))
    i+=1
  while j < m:
    result.append(b.get(j))
    j+=1
  return result

def merge_sort(a):
  n = a.__len__()
  # Base Case
  if n <= 1 :
    return a

  left = slice_array(a,0,n//2)
  right = slice_array(a,n//2,n)
  left = merge_sort(left)
  right = merge_sort(right)
  result = merge(left, right)
  return result