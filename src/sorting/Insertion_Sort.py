import sys
import os
from sorting.Get_Key import key
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath('src/models/Get_Key.py'))))
def insertion_sort(a):
  n = a.__len__()
  for i in range(1,n):
    idx = i
    j = i-1
    while j>=0:
      if key(a.get(j)) < key(a.get(idx)):
        break
      temp = a.get(j)  # To swap values
      a.set(j, a.get(idx))
      a.set(idx, temp)
      idx = j
      j = j-1
  return a
