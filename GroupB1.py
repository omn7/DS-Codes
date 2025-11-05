from collections import deque

class EventQueue:
    def __init__(self):
        self.queue = deque()
    
    def add_event(self, event):
        self.queue.append(event)
    
    def process_next_event(self):
        if self.queue:
            return self.queue.popleft()
        else:
            return "No events to process"
    
    def display_pending_events(self):
        return list(self.queue)
    
    def cancel_event(self, event):
        if event in self.queue:
            self.queue.remove(event)
            return f"Event '{event}' cancelled."
        return "Event not found."

# Example Usage
eq = EventQueue()
eq.add_event("Event1")
eq.add_event("Event2")
print("Pending Events:", eq.display_pending_events())
print("Processing:", eq.process_next_event())
print(eq.cancel_event("Event2"))
print("Pending Events:", eq.display_pending_events())
