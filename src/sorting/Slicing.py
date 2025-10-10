from models.ArrayList import DynamicArray
def slice_array(A,start,stop,step=1):
  result = DynamicArray()
  n = A.__len__()
  if start<0:
    start = 0
  if stop > n :
    stop = n
  for i in range(start,stop,step):
    result.append(A.get(i))
  return result