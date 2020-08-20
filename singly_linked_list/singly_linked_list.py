
class Node:
    def __init__(self, value, next=None):
        # value at linked_list node
        self.value = value       
         #next node in the list
        self.next = next


class LinkedList: 
    def __init__(self):
        self.head = None # pointd to first node in list
        self.tail = None # points to last node in list
        self.length = 0

    def __str__(self):
        pass

    # append /add --> add_to_tail
    def add_to_tail(self, value):
        # check if there's a tail:
        # If no, empty list
        if not self.tail:
            new_tail = Node(value, None)
            self.head = new_tail
            self.tail = new_tail

        else: 
            #create a new node with the value we want to add
            new_tail = Node(value, None)
            # set current tail.next to the new node
            self.tail.next = new_tail
            # set self.tail to new node
            self.tail = new_tail             
        self.length = self.length + 1

        
    # remove / remove -->  remove_HEAD
    def remove_head(self):
        # if no head(empty list)
        if not self.head:
            return None
        
        # List w only one element
        if self.head == self.tail:
            # set self.head to current_head.next / None
            current_head = self.head
            self.head = None
            self.tail = None
            # Decrement length by 1
            self.length = self.length - 1
            return current_head.value

        # If head (General Case)
        else:
            # Set self.head to current_head.next
            current_head = self.head
            self.head = current_head.next
            self.length = self.length - 1
            return current_head.value

    def remove_tail(self):
        # check if it's there        
        if not self.tail:
            return None

        # List of one node        
        if self.tail == self.head:
            # save current_tail value
            current_tail = self.tail
            self.head = None
            self.tail = None
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
        self.length = self.length -1
        return value