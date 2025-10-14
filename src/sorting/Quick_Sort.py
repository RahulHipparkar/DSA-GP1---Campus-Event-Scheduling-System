from src.sorting.Get_Key import key
def find_pivot(arr, low, high):
  pivot = arr.get(low)
  i = low +1
  j = high

  while True:
    while i<= high and key(arr.get(i))<=key(pivot):
      i+=1
    while j>=low +1 and key(arr.get(j))> key(pivot):
      j-=1
    if i >= j:
      break

    # This swap should be outside the inner while loops
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
    if low<p_index-1:
      qs(arr,low,p_index-1)
      qs(arr,p_index+1,high)

def quick_sort(arr, low, high):
    qs(arr, low, high)
    return arr