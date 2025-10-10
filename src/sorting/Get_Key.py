from models.event import Event
def key(event):
    return (event.date, event.time)