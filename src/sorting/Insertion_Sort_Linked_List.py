from src.sorting.Get_Key import key
from src.models.LinkedList import Node
def insertion_sort_linked_list(List):
  dummy = Node(0)
  cur = List.head

  while cur:
    prev = dummy
    while prev.next and key(prev.next.value)<=key(cur.value):
      prev = prev.next
    nxt = cur.next
    cur.next = prev.next
    prev.next = cur
    cur = nxt
  List.head = dummy.next
