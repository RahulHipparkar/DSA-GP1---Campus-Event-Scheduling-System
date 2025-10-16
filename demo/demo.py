"""
This file is just for testing the code and different functions
"""
import os, sys
# Go up one level (from demo/ → project_root/)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from src.models.event import Event
from src.models.ArrayList import DynamicArray
from src.models.LinkedList import LinkedList
from src.searching.Linear_Search import linear_search
from src.searching.Binary_Search import binary_search
from src.sorting.Get_Key import key
from src.sorting.Insertion_Sort import insertion_sort
from src.sorting.Slicing import slice_array
from src.sorting.Merge_Sort import merge_sort
from src.sorting.Quick_Sort import quick_sort
from src.sorting.Insertion_Sort_Linked_List import insertion_sort_linked_list
from src.sorting.Merge_Sort_Linked_List import merge_sort_list
from src.sorting.Quick_Sort_Linked_List import quickSort
from src.searching.Conflict_Detection import display_conflicts
e1 = Event(101,'Midterm','2025-10-06','18:00','Duane')
e2 = Event(102, 'Carrer Event', '2025-10-06', '12:00','UMC' )
e3 = Event(103,'In class Activity', '2025-10-05', '11:00', 'Beca')
e4 = Event(104,'Carrer Fair','2025-10-07', '11:00', 'UMC')
ll = LinkedList()
ll.push(e1)
ll.append(e2)
ll.append(e3)
ll.insertAt(1,e4)
ll.head = quickSort(ll.head)
# print(ll)
a = DynamicArray()
a.append(e1)
a.append(e2)
a.append(e3)
a.insert(e4,1)
# print(a.list_all())
# print(linear_search(a,103))
ex = Event(201, "EventX","2025-10-11","4:30","X")
ey = Event(202, "EventX","2025-10-11","4:30","Y")
ez = Event(203,"EventZ","2025-10-11","4:30","Z" )
events = LinkedList()
events.append(ex)
events.append(ey)
events.append(ez)
# display_conflicts(events)
# arr = quick_sort(a,0,len(a)-1)
# print(arr.list_all())
print(ll.search_by_id(106))