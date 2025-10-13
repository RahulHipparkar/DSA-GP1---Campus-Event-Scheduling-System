import pytest
from src.models.LinkedList import LinkedList
from src.models.event import Event
@pytest.fixture
def sample_events():
    return[
        Event(101, "Midterm", "2025-10-05", "09:00", "Duane"),
        Event(102, "Seminar", "2025-10-06", "11:00", "ECCR"),
        Event(103, "Workshop", "2025-10-07", "10:00", "CASE"),
    ]

def test_dynamic_array(sample_events):
    linked_list = LinkedList()
    for e in sample_events:
        linked_list.append(e)
    assert len(linked_list) == len(sample_events),'❌ Linked list fails to append events'
    for i in range(len(sample_events)):
        event = linked_list.get(i)
        assert event.id == sample_events[i].id,'❌ Linked list fails to access event'
    print('✅ Linked List is able to append and access events successfully')

