import my_slinked_list as SLL

class Stack:
    def __init__(self):
        # the stack must use this singly linked-list to store the items
        self.items = SLL.SinglyLinkedList()
    
    def is_empty(self):
        return self.items.size == 0

    
    def push(self, item):
        "adds an item at the top of the stack"
        self.items.append(item)
    
    
    def pop(self):
        "removes and returns the item at the top of the stack"
        length = self.items.length()
        
        # if not empty
        if length != 0:
          delete = self.items.delete(length-1)
          return delete
        # if empty
        else:
          return "the stack is empty"