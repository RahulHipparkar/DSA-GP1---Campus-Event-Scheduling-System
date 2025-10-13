import pytest
from src.models.ArrayList import DynamicArray
from src.models.event import Event
from src.searching.Conflict_Detection import find_conflicts
@pytest.fixture
def sample_events():
  arr = DynamicArray()
  arr.append(Event(101, "Midterm", "2025-10-05", "09:00", "Duane"))
  arr.append(Event(102, "Seminar", "2025-10-05", "09:00", "ECCR"))
  arr.append(Event(103, "Hackathon", "2025-10-07", "14:00", "UMC"))
  arr.append(Event(104, "Workshop", "2025-10-08", "10:00", "CASE"))
  return arr

def test_find_conflicts(sample_events):
  arr = sample_events
  conflicts = find_conflicts(arr)
  assert len(conflicts)>0, "❌ function failed to find any conflicts"
  print("✅  Test case passed - function is able to find conflicts")