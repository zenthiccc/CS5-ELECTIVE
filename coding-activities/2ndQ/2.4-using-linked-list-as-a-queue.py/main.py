import slinked_list as SLL

class Queue:
    def __init__(self):
        # the queue must use this singly linked-list to store the items
        self.items = SLL.SinglyLinkedList()

    # IMPLEMENT
    def enqueue(self, item):
        "adds an item at the end of the queue"
        self.items.append(item)

    # IMPLEMENT
    def dequeue(self):
        "removes and returns the item at the start of the queue"
        length = self.items.length()
        
        # if not empty
        if length != 0:
          delete = self.items.delete(0)
          return delete
        # if empty
        else:
          return "the queue is empty"