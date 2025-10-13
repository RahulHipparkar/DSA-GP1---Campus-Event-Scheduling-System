from src.sorting.Get_Key import key
def getTail(current):
  while current and current.next:
    current = current.next
  return current

def partition(head, tail):
  pivot = head

  prev = head
  current = head

  while current != tail.next:
    if key(current.value) < key(pivot.value):
      current.value, prev.next.value = prev.next.value, current.value # swap

      prev = prev.next
    current = current.next # move to next node
  pivot.value, prev.value = prev.value, pivot.value
  return prev

def quickSort_ll(head, tail):
  if head is None or head == tail:
    return

  pivot = partition(head, tail)
  quickSort_ll(head, pivot) # from start to middle
  quickSort_ll(pivot.next, tail) # from middle to end

def quickSort(head):
    tail = getTail(head) # earlier function
    quickSort_ll(head, tail)
    return head