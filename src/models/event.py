class Event:
  def __init__(self, id, title, date, time, location):
    self.id = id
    self.title = title
    self.date = date # yyyy-mm-dd
    self.time = time # 24 hour format
    self.location = location

  def __repr__(self):
    # return a list-like display
    return f"[{self.id}, '{self.title}', '{self.date}', '{self.time}', '{self.location}']"