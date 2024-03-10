"""
<TODO>
"""


# ------------------------------ Exceptions -------------------------------------
class UndocumentedError(Exception):
    pass


class QueueCapacityTypeError(Exception):
    pass


"""Raises an error if the queue capacity is not of type int"""


class QueueCapacityBoundError(Exception):
    pass


"""Raises an error if the queue capacity is not a positive int"""


class QueueIsFull(Exception):
    pass


"""Raises an exception if, upon enqueue-ing, the queue reaches its capacity limit"""


class QueueIsEmpty(Exception):
    pass


"""Raises an exception if, upon dequeue-ing, the queue is empty"""


class StackCapacityTypeError(Exception):
    pass


"""Raises an error if the stack capacity is not of type int"""


class StackCapacityBoundError(Exception):
    pass


"""Raises an error if the stack capacity is a negative int"""


class StackIsFull(Exception):
    pass


"""Raises an exception if, upon pushing, the stack is full"""


class StackIsEmpty(Exception):
    pass


"""Raises an exception if, upon popping, the stack is empty"""

# ---------------------------------- Classes -----------------------------------


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    pass


"""This method takes one parameter, 'data', which is used to initialize
    the data attribute. The next attribute is initialized to be 
    'none' by default. Complexity: O(1)."""


class Queue:
    def __init__(self, capacity):
        if not isinstance(capacity, int):
            raise QueueCapacityTypeError("Queue capacity must be of type int")
        if capacity <= 0:
            raise QueueCapacityBoundError("Queue capacity must be a positive int")
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.currentSize = 0


"""Init is called when a new instance of the class is created, and takes one parameter,
   'capacity'. If capacity is not of type int of is a negative int,
   the function raises the errors defined above. The head and tail
   are initialized to 'non' and the current size is 0. Complexity: O(1)."""


def enqueue(self, data):
    if self.currentSize < self.capacity:
        new.node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
            self.currentSize += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.currentSize += 1
    else:
        raise QueueIsFull("Queue is full")


"""Enqueue takes one parameter, 'data', which is added to the queue
   and updates the currentSize and tail. Complexity: O(1)."""


def dequeue(self):
    if self.currentSize > 0:
        temp = self.head
        self.head = self.head.next
        self.currentSize -= 1
        return temp.data
    else:
        raise QueueIsEmpty("Queue is empty")


"""Dequeue removes an item from the queue and updates the currentSize and head.
   Complexity: O(1)."""


def front(self):
    if self.currentSize > 0:
        return self.head.data
    else:
        raise QueueIsEmpty("Queue is empty")


"""Simply returns data of the head node if the queue is not empty. Otherwise returns false.
   Complexity: O(1)."""


def isEmpty(self):
    return self.currentSize == 0


"""Returns true if the currentSize of the queue is 0, false otherwise.
   Complexity: O(1)."""


def isFull(self):
    return self.currentSize == self.capacity


"""Returns true if the currentSize is equal to capacity, false otherwise.
   Complexity: O(1)."""


pass


class Stack:
    def __init__(self, capacity):
        if not isinstance(capacity, int):
            raise StackCapacityTypeError("Stack capacity must be of type int.")
        if capacity <= 0:
            raise StackCapacityBoundError("Stack capacity must be a positive int.")
        self.head = None
        self.capacity = capacity
        self.currentSize = 0


"""Initializes a stack and checks for the correct parameters. 
   Assigns a 'none' value to the head and initializes the stack
   to a have a currentSize of 0. Complexity: O(1)."""


def push(self, item):
    if self.currentSize < self.capacity:
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.currentSize += 1
    else:
        raise StackIsFull("Stack is full")


"""The push method pushes an item to the top of the stack by creating
   a new node. The new node's next points to the current head and sets
   the new node as the new head. Complexity: O(1)."""


def pop(self):
    if self.currentSize > 0:
        temp = self.head
        self.head = self.head.next
        self.currentSize -= 1
        return temp.data
    else:
        raise StackIsEmpty("Stack is empty")


"""The pop method removes the head of the stack, making the next node
   the head and returning the value of the removed node.
   Complexity: O(1)."""


def peek(self):
    if self.currentSize > 0:
        return self.head.data
    else:
        raise StackIsEmpty("Stack is empty")


"""The peek method returns the value of the head node without
   removing it from the stack. Complexity: O(1)."""


def isEmpty(self):
    return self.currentSize == 0


"""Returns true if the currentSize of the stack is 0. Returns false otherwise.
   Complexity: O(1)."""


def isFull(self):
    return self.currentSize == self.capacity


"""Returns true if the currentSize of the stack is its capacity. Returns false otherwise.
   Complexity: O(1)."""
pass
# ------------------------------------------------------------------------------
