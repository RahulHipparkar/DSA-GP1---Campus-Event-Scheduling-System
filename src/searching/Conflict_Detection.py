def find_conflicts(events):
  """
  This function prints conflicted events. It uses dictionary data structure to store the conflicted events
  """
  n = events.__len__()
  time_to_events = {} 
  for i in range(n):
    ev = events.get(i)
    key = (ev.date, ev.time)
    if key not in time_to_events:
      time_to_events[key] = []
    time_to_events[key].append(ev)
  overlapping = {k:v for k,v in time_to_events.items() if len(v)>=2}
  for (date, time), conflicts in overlapping.items():
    print(f"\nConflicted events on {date}")
    for e in conflicts:
      print(f" ID = {e.id}, Title = {e.title}, Location ={e.location}")