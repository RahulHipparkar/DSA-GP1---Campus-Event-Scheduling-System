def sort(a):
  n = a.__len__()
  for i in range(1,n):
    idx = i
    j = i-1
    while j>=0:
      if a.get(j).id < a.get(idx).id:
        break
      temp = a.get(j)  # To swap values
      a.set(j, a.get(idx))
      a.set(idx, temp)
      idx = j
      j = j-1
  return a

def binary_search(arr,target_id):
  arr = sort(arr)
  start = 0
  end = arr.__len__()-1
  while start <= end:
    mid = (start+end)//2
    if arr.get(mid).id==target_id:
      return f"Event with id {arr.get(mid).id} was found"
    elif target_id < arr.get(mid).id:
      end = mid-1
    else:
      start = mid+1
  return f"Event is not found"