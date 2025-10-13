def linear_search(arr,target_id):
  for i in range(arr.__len__()):
    if arr.get(i).id == target_id:
      return f"Event with id {arr.get(i).id} is found"
  return f"Event is not found"
