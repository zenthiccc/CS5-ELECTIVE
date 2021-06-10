import slinked_list as SLL

class Stack:
    def __init__(self):
        # the stack must use this singly linked-list to store the items
        self.items = SLL.SinglyLinkedList()
    
    # IMPLEMENT
    def push(self, item):
        "adds an item at the top of the stack"
        
        self.items.append(item)

    
    # IMPLEMENT
    def pop(self):
        "removes and returns the item at the top of the stack"
        # implement the pop operation of the stack here
        length = self.items.length()
        
        # if not empty
        if length != 0:
          delete = self.items.delete(length-1)
          return delete
        # if empty
        else:
          return "the stack is empty"