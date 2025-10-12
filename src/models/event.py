class Event:
  def __init__(self, id, title, date, time, location):
    self.id = id
    self.title = title
    self.date = date # yyyy-mm-dd
    self.time = time # 24 hour format
    self.location = location

  def __repr__(self):
    # return a event object as dictionary
     e = {"Id":self.id, "Title":self.title, "Date":self.date,"Time":self.time,"Location":self.location}
     return f"{e}"