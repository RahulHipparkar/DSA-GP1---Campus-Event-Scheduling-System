import pytest
from src.models.ArrayList import DynamicArray
from src.models.event import Event
@pytest.fixture
def sample_events():
    return[
        Event(101, "Midterm", "2025-10-05", "09:00", "Duane"),
        Event(102, "Seminar", "2025-10-06", "11:00", "ECCR"),
        Event(103, "Workshop", "2025-10-07", "10:00", "CASE"),
    ]

def test_dynamic_array(sample_events):
    arr = DynamicArray()
    for e in sample_events:
        arr.append(e)
    assert len(arr) == len(sample_events),'❌ Dynamic Array fails to append events'
    for i in range(len(sample_events)):
        event = arr.get(i)
        assert event.id == sample_events[i].id,'❌ Dynamic Array fails to access event'
    print('✅ Dynamic Array is able to append and access events successfully')

