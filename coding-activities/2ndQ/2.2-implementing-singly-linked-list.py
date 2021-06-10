class Node:        
    def __init__(self, item):
        self.item = item
        self.next = None

class SinglyLinkedList:
    "This is an implementation of a singly linked-list."
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
  
    # use this print function to test your list
    def print_list(self):
        "displays to the console the items in the list"
        list_str = "[ "
        current = self.head
        while current is not None:
            list_str += str(current.item) + " "
            current = current.next
        print(list_str + "]")
        
    def length(self):
        current = self.head
        length = 0
        while current.next is not None:
          length += 1
          current = current.next
        return length

    # IMPLEMENT
    def append(self, item):
      "adds item to the end of the list"
      # implement the append operation here
      # please delete this 'pass' here if you start coding
      new_node = Node(item)
      if self.head is None:
        self.head= new_node
        
      else:
        current = self.head
        while current.next is not None:
          current = current.next
        current.next = new_node


    # IMPLEMENT
    def delete(self, index):
        "removes and returns the item in the list at specified index"
        
        if index < 0 or index > self.length() - 1:
            print("Invalid index!")
            return None
            
        # implement the delete operation here
        # return the item inside the target/deleted node
        
        if index == 0:
          current = self.head
          self.head = current.next
          delete = current.item
          current = None
          
          return delete
        
        else:
          current = self.head
          previous = None 
          while index != 0:
            previous = current
            current = current.next
            index -= 1
          
          previous.next = current.next
          delete = current.item
          current = None
          
          return delete