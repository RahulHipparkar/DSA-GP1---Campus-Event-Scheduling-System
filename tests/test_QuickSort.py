import pytest
from src.models.event import Event
from src.models.ArrayList import DynamicArray
from src.sorting.Quick_Sort import quick_sort
@pytest.fixture
def sample_events():
  arr = DynamicArray()
  arr.append(Event(101, "Midterm", "2025-10-08", "09:00", "Duane"))
  arr.append(Event(102, "Seminar", "2025-10-09", "11:00", "ECCR"))
  arr.append(Event(103, "Hackathon", "2025-10-07", "14:00", "UMC"))
  arr.append(Event(104, "Workshop", "2025-10-05", "10:00", "CASE"))
  return arr

def test_quick_sort(sample_events):
  sorted_events = quick_sort(sample_events,0,len(sample_events)-1)
  result = [(e.date,e.time) for e in sorted_events.list_all()]
  expected = sorted([(e.date, e.time) for e in sample_events.list_all()])
  assert result == expected, "❌ Quick Sort failed to sort dynamic array of events"
  print("✅  Quick sort passed - Events are sorted correctly by date and time")