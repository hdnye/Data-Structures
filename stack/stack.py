"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.

3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
import time
from singly_linked_list import LinkedList

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         # Add to back 
#         self.storage.append(value)

#     def pop(self):
#         if len(self.storage) == 0:
#             return None
#         # Remove from back 
#         return self.storage.pop()

# n = 100000
# stack = Stack()
# start = time.time()
# for i in range(n):
#     stack.push(1)
# print('Pushing to back: ', time.time() - start)

# n = 100000
# stack = Stack()
# start = time.time()
# for i in range(n):
#     stack.pop()
# print('Popping from back: ', time.time() - start)

'''
2. Re-implement the Stack class, this time using the linked list implementation
as the underlying storage structure.
Make sure the Stack tests pass.
'''

class Stack(): 
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
     
    def __len__(self):
        return self.size

    def push(self, value):
           # Add to tail 
        self.storage.add_to_tail(value)
        self.size +=1

    def pop(self):
        if self.size == 0:
            return None
        # Remove from tail 
        self.size -=1
        return self.storage.remove_tail()
       
 
