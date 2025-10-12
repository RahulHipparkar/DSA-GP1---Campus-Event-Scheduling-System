from sorting.Get_Key import key
def find_pivot(arr, low, high):
  pivot = arr.get(low)
  i = low
  j = high
  while i < j:
    while key(arr.get(i))<= key(pivot) and i <= high - 1:
      i+=1
    while key(arr.get(j))> key(pivot) and j>=low + 1:
      j-=1
    if i < j:
      temp = arr.get(i)
      arr.set(i,arr.get(j))
      arr.set(j,temp)
  temp = arr.get(low)
  arr.set(low,arr.get(j))
  arr.set(j, temp)
  return j

def qs(arr,low,high):
  if low < high:
    p_index = find_pivot(arr, low,high)
    qs(arr, low, p_index -1)
    qs(arr, p_index+1, high)

def quick_sort(arr):
  n = arr.__len__()
  qs(arr, 0, n-1)
  return arr