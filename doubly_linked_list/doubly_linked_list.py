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
        pass
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        pass
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        pass
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        pass
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
       # Check for empty pointers
       if self.length == 0:
           return None
       # Get prev node = node.prev
       prev_node = node.prev
       # Set prev_node.next to node.next
       prev_node.next = node.next
       # Set next_node to node.next
       next_node = node.next
       # Set next_node to point to prev_node
       next_node.prev = prev_node
       # Decrement length 
       self.length -= 1
       # Remove pointers from deleted node:
       #    set node.prev to none 
       node.prev = None
       #    set node.next to none
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