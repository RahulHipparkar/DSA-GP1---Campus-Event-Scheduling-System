from sorting.Get_Key import key
from models.LinkedList import Node
def merge_sort_list(head):
  if not head or not head.next:
    return head

  mid = findMid(head)
  left = merge_sort_list(head)
  right = merge_sort_list(mid)
  return merge_list(left,right)

def merge_list(List1, List2):
  dummy = Node(0)
  tail = dummy
  while List1 and List2:
    if key(List1.value) <= key(List2.value):
      tail.next = List1
      List1 = List1.next
    else:
      tail.next = List2
      List2 = List2.next
    tail = tail.next
  tail.next = List1 if List1 else List2
  return dummy.next


def findMid(head):
  midPrev =None
  while head and head.next:
    midPrev = head if not midPrev  else midPrev.next
    head = head.next.next
  mid = midPrev.next
  midPrev.next = None
  return mid