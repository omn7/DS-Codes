from collections import deque
class CallCenterQueue:
    def __init__(self):
        self.queue = deque()
    
    def addCall(self, customerID, callTime):
        self.queue.append((customerID, callTime))
    
    def answerCall(self):
        if self.queue:
            return self.queue.popleft()
        return "No calls to answer"
    
    def viewQueue(self):
        return list(self.queue)
    
    def isQueueEmpty(self):
        return len(self.queue) == 0

# Example usage
ccq = CallCenterQueue()
ccq.addCall(101, 15)
ccq.addCall(102, 10)
print("Queue:", ccq.viewQueue())
print("Answering:", ccq.answerCall())
print("Is queue empty?", ccq.isQueueEmpty())
