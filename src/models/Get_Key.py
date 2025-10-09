from src.models import Event
def key(event):
    return (event.date, event.time)