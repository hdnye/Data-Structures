"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    def get_value(self):
        return self.value        
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

       
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
           # Is there a head?
           # Create new node
        if not self.head: 
            new_head = ListNode(value, None)
           # Point to head/tail
            self.head = new_head
            self.tail = new_head
           # Increment length
            self.length +=1
          # If head:
        else: 
            # Create new head
            new_head = ListNode(value, None)
            # set pointer to new head
            new_head.next = self.head
            # Set self. head = new_head
            self.head = new_head
            self.length +=1
        # return new_node value
        return new_head.value
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
            # If no head/empty []
        if not self.head:
            return None
            # If only 1 element
        if self.head == self.tail: 
            cur_head = self.head
            self.head = None
            self.tail = None
            # decrement list
            self.length -=1
            # return cur_value
            return cur_head.value
            # Else set new head
        else: 
            cur_head = self.head
            # set pointer to next node
            self.head = cur_head.next
            # decrement list
            self.length -=1
            # rtn value
        return cur_head.value
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
            # check if there's a tail:
            # If no, empty list
        if not self.tail:
            new_tail = ListNode(value)
            # Point to head/tail
            self.head = new_tail
            self.tail = new_tail
            # Increment length
            self.length +=1
            # If tail:
        else:
            #create a new node with the value we want to add
            new_tail = ListNode(value, None)
            new_tail.prev = self.tail
            # set current tail.next to the new node
            self.tail.next = new_tail
            # set self.tail to new node
            self.tail = new_tail
            self.length += 1
        return new_tail.value
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # check if it's there
        if not self.tail:
            return None

        # List of one node
        if self.tail == self.head:
            # save current_tail value
            current_tail = self.tail
            # set to none
            self.head = None
            self.tail = None
            # return current value
            return current_tail.value

        # General case start at head & iterate to next-to-last node
        # stop when current_node == self.tail
        node = self.head
        while node.next != self.tail:
            node = node.next
        # save the current_tail value
        value = self.tail.value
        # set self.tail to current_value
        self.tail = node
        # set node.next to none
        node.next = None
        self.length = self.length - 1
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
       self.delete(node)
       self.add_to_head(node.value)

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)
     
    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        prev_node = node.prev
         # Check for empty pointers
        if self.length == 0:
           return None
         # If head == node
        if prev_node is None:
           self.head = node.next 
         # Get prev node = node.prev
        else:   
          # Set prev_node.next to node.next
            prev_node.next = node.next
          # Set next_node to node.next
        next_node = node.next
          # Set next_node to point to prev_node
        if next_node == None:
             self.tail = node.prev
        else: 
            next_node.prev = prev_node
          # Decrement length 
        self.length -= 1
          # Remove pointers from deleted node:
          # set node.prev to none 
        node.prev = None
          # set node.next to none
        node.next = None
          # return node.value
        return node.value
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
         # if len = 0 return none
        if self.length == 0:
            return None
         # if len = 1
        if self.length == 1:
            return self.head.value

         # cur_max starts as head.value
        cur_max = self.head.value

         # Starrt current node at head
        cur_node = self.head

          # Then iterate through the list
          # stop when cur_node is none
        while cur_node is not None:
             # compare cur_max to each val & update cur_max
            if cur_max < cur_node.value:
                cur_max = cur_node.value
             # move cur_node forward
            cur_node = cur_node.next
              # return cur_max
            return cur_node
