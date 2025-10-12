from models.event import Event
from models.ArrayList import DynamicArray
from models.LinkedList import LinkedList
from searching.Linear_Search import linear_search
from searching.Binary_Search import binary_search
from sorting.Get_Key import key
from sorting.Insertion_Sort import insertion_sort
from sorting.Slicing import slice_array
from sorting.Merge_Sort import merge_sort
from sorting.Quick_Sort import quick_sort
from sorting.Insertion_Sort_List import insertion_sort_list
from sorting.Merge_Sort_List import merge_sort_list
from searching.Conflict_Detection import find_conflicts
e1 = Event(101,'Midterm','2025-10-06','18:00','Duane')
e2 = Event(102, 'Carrer Event', '2025-10-06', '12:00','UMC' )
e3 = Event(103,'In class Activity', '2025-10-05', '11:00', 'Beca')
e4 = Event(104,'Carrer Fair','2025-10-07', '11:00', 'UMC')
ll = LinkedList()
ll.push(e1)
ll.append(e2)
ll.append(e3)
ll.insertAt(1,e4)
# ll.head = merge_sort_list(ll.head)
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
find_conflicts(events)