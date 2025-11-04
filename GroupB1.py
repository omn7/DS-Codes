from collections import deque

class EventQueue:
    def __init__(self):
        self.queue = deque()

    def add_event(self, event):
        # Add an event to the end of the queue
        self.queue.append(event)
        print(f"Event '{event}' added.")

    def process_next_event(self):
        # Process and remove the oldest event from the queue
        if self.queue:
            event = self.queue.popleft()
            print(f"Processing event: '{event}'")
            return event
        else:
            print("No events to process.")
            return None

    def display_pending_events(self):
        # Display all events waiting to be processed
        if self.queue:
            print("Pending events in queue:", list(self.queue))
        else:
            print("No pending events.")

    def cancel_event(self, event):
        # Cancel an event if it is pending
        try:
            self.queue.remove(event)
            print(f"Event '{event}' canceled.")
        except ValueError:
            print(f"Event '{event}' not found or already processed.")


# Example usage
events = EventQueue()
events.add_event("LoginRequest")
events.add_event("Payment")
events.display_pending_events()
events.process_next_event()
events.display_pending_events()
events.cancel_event("Payment")
events.display_pending_events()
