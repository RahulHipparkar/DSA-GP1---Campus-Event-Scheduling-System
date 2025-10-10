from models.event import Event
from models.ArrayList import DynamicArray
from models.LinkedList import LinkedList
# from sorting.Get_Key import key
from sorting.Insertion_Sort import insertion_sort
from sorting.Slicing import slice_array
from sorting.Merge_Sort import merge_sort
e1 = Event(101,'Midterm','2025-10-06','18:00','Duane')
e2 = Event(102, 'Carrer Event', '2025-10-06', '12:00','UMC' )
e3 = Event(103,'In class Activity', '2025-10-05', '11:00', 'Beca')
e4 = Event(104,'Carrer Fair','2025-10-07', '11:00', 'UMC')
a = DynamicArray()
a.append(e1)
a.append(e2)
print(a.get(1))
a.append(e3)
a.insert(e4,1)
# a.remove(1)
a = insertion_sort(a)
print(a.list_all())
