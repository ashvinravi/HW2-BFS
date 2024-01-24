class Queue():
    """
    Class to contain queue and pop/append function.
    Queue works as first in, first out. 
    """
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.insert(0, item)
    
    def pop(self):
        return self.queue.pop()
    
    def size(self):
        return len(self.queue)
    
    def isEmpty(self):
        return self.size() == 0
