import pytest
from src.models.ArrayList import DynamicArray
from src.models.event import Event
from src.searching.Binary_Search import binary_search
from src.searching.Binary_Search import sort
@pytest.fixture
def sample_events():
  arr = DynamicArray()
  arr.append(Event(103, "Midterm", "2025-10-07", "09:00", "Duane"))
  arr.append(Event(102, "Seminar", "2025-10-09", "11:00", "ECCR"))
  arr.append(Event(101, "Hackathon", "2025-10-08", "14:00", "UMC"))
  arr.append(Event(104, "Workshop", "2025-10-05", "10:00", "CASE"))
  return arr

def test_linear_search(sample_events):
  target_id = 103
  arr = sort(sample_events)
  message = binary_search(arr,target_id)
  assert message == f"Event with id {target_id} was found", "❌ Binary Search failed to search an event by id"
  print("✅  Binary search passed - Event found successfully")