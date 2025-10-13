import pytest
from src.models.LinkedList import LinkedList
from src.models.event import Event
from src.sorting.Insertion_Sort_Linked_List import insertion_sort_linked_list
@pytest.fixture
def build_linked_list():
  def _builder(events):
    List = LinkedList()
    for e in events:
        List.append(e)
    return List
  return _builder

@pytest.fixture
def extract_tuples():
  def _extractor(ll):
    res = []
    head = ll.head
    current = head
    while current:
        e = current.value
        res.append((e.date, e.time))
        current = current.next
    return res
  return _extractor

@pytest.fixture
def sample_events():
  List = []
  List.append(Event(101, "Midterm", "2025-10-09", "09:00", "Duane"))
  List.append(Event(102, "Seminar", "2025-10-08", "09:00", "ECCR"))
  List.append(Event(103, "Hackathon", "2025-10-07", "14:00", "UMC"))
  List.append(Event(104, "Workshop", "2025-10-05", "10:00", "CASE"))
  return List

def test_insertion_sort_linked_list(sample_events, build_linked_list,extract_tuples):
  ll = build_linked_list(sample_events)
  insertion_sort_linked_list(ll)
  sorted_events = extract_tuples(ll)
  expected = sorted((e.date,e.time) for e in sample_events)
  assert sorted_events == expected, "❌ Insertion Sort failed to sort linked list of events"
  print("✅  Insertion sort passed - Events are sorted correctly by date and time")