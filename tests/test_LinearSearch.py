import pytest
from src.models.ArrayList import DynamicArray
from src.models.event import Event
from src.searching.Linear_Search import linear_search
@pytest.fixture
def sample_events():
  arr = DynamicArray()
  arr.append(Event(101, "Midterm", "2025-10-05", "09:00", "Duane"))
  arr.append(Event(102, "Seminar", "2025-10-06", "11:00", "ECCR"))
  arr.append(Event(103, "Hackathon", "2025-10-07", "14:00", "UMC"))
  arr.append(Event(104, "Workshop", "2025-10-08", "10:00", "CASE"))
  return arr

def test_linear_search(sample_events):
  target_id = 103
  arr = sample_events
  message = linear_search(arr,target_id)
  assert message == f"Event with id {target_id} is found", "❌ Linear Search failed to search an event by id"
  print("✅  Linear search passed - Event found successfully")