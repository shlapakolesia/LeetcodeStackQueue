'''Implement Stack using Queues'''

class Node:
    '''class Node'''
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    '''class Queue'''
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, x):
        '''Add element to the back'''
        new_node = Node(x)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node

    def pop(self):
        '''Remove and return front element'''
        val = self.head.val
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return val

    def peek(self):
        '''Return front element'''
        return self.head.val

    def empty(self):
        '''Check if queue is empty'''
        return self.head is None

class MyStack:
    '''class MyStack'''

    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, x: int) -> None:
        '''Push element to top'''
        self.queue2.push(x)
        while not self.queue1.empty():
            self.queue2.push(self.queue1.pop())

        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        '''Remove and return top element'''
        return self.queue1.pop()

    def top(self) -> int:
        '''Return top element'''
        return self.queue1.peek()

    def empty(self) -> bool:
        '''Check if stack is empty'''
        return self.queue1.empty()
