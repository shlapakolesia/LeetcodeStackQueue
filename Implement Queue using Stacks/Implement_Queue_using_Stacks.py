'''Implement Queue using Stacks'''

class Node:
    '''class Node'''
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Stack:
    '''class Stack'''
    def __init__(self):
        self.head = None

    def push(self, item):
        '''Push element'''
        node = Node(item)
        node.next = self.head
        self.head = node

        # self.head = Node(item, next=self.head)

    def pop(self):
        '''Remove and return top element'''
        val = self.head.val
        self.head = self.head.next
        return val

    def peek(self):
        '''Return top element'''
        return self.head.val

    def empty(self):
        '''Check if stack is empty'''
        return self.head is None

class MyQueue:
    '''class MyQueue'''

    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def push(self, x: int) -> None:
        '''Add element to the back'''
        self.stack_in.push(x)

    def pop(self) -> int:
        '''Remove and return front element'''
        if self.stack_out.empty():
            while not self.stack_in.empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self) -> int:
        '''Return front element'''
        if self.stack_out.empty():
            while not self.stack_in.empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.peek()

    def empty(self) -> bool:
        '''Check if queue is empty'''
        return self.stack_in.empty() and self.stack_out.empty()
