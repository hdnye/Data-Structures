
class Node:
    def __init__(self, value, next=None):
        self.value = value       
        self.next = next #next node in the list


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
        # If no, exmpty list
        if not self.tail:
            new_tail = Node(value, None)
            self.head = new_tail
            self.tail = new_tail

        else: 
            new_tail = Node(value, None)
            old_tail = self.tail
            old_tail.next = new_tail
            self.head = new_tail
        self.length += 1

        
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

        # List of one element
        # save current_tail value
        if self.tail == self.head:
            current_tail = self.tail
            self.head = None
            self.tail = None
            return current_tail.value
            
        # if not, start at head & iterate to next-to-last node
        # stop when current_node == self.tail   
        # save the current_tail value
        # set self.tail to current_value
        else:
            current_tail = self.tail
            self.tail = current_tail.next
            self.length = self.length - 1
            return current_tail.value
