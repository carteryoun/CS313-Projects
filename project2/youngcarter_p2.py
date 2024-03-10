#============================= Instructor Comments =============================
# Overall: grade Submission
# Correctness: 50/60 pts
# Completeness: 25/25 pts
# Elegence: 15/15 pts
# Extra credit: 0/10 pts
# Total: 90/100 pts
# Grade: 
#
#======================== Unit Testing Results (Complex) =======================
# Section-01: Method Validation Tests (Correct/Complete)
# Test-01: Valid Constructor Implementation (Queue/Stack/Node) - FAIL
#    ERROR: Required instance variable <PriorityQueue>._heap does not exist
# Test-02: Valid Insert Implementation - FAIL
#    ERROR: Failed heap validation - (False, "Invalid heap detected: Child-6 (25, 'data') > parent-2 (20, 'data')").
#                       (30, 'data')                        
#         (10, 'data')                 (20, 'data')         
#  (5, 'data')  (7, 'data')   (15, 'data')  (25, 'data')  
# Test-03: Valid extractMax Implementation - PASS
# Test-04: Valid peekMax() Implementation - FAIL
#    ERROR: <PriorityQueue>.peekMax() crashed on valid call when PQ is empty.
#        Exception: QueueIsEmpty('The queue is empty.')
# Test-05: Valid isEmpty() Implementation - PASS
# Test-06: Valid isFull() Implementation - PASS
#
# Section-02: Proper Error Handeling Tests
# Error Test-01: Proper Constructor Error Handeling - FAIL
#    Warning: Could not find required exception - PriorityQueueCapacityBoundError, but found the QueueCapacityBoundError
#    Warning: Could not find required exception - PriorityQueueCapacityTypeError, but found the QueueCapacityTypeError
#    ERROR: Either raised the wrong exception or did not raise an exception on invalid call <PriorityQueue>(None).
# Error Test-02: Proper Insert Error Handeling - PASS
# Error Test-03: Proper ExtractMax Error Handeling - PASS
#
# Section-3 (Extra Credit): Sorted Array (heap_sort) - FAIL
#    ERROR: Could not find required exception - InputError
#================================ End of Testing ===============================
#===============================================================================


# ============================== Exceptions =====================================


class QueueCapacityTypeError(Exception):
    """
    This exception gets raised when the queue is given the wrong type.
    """
    pass


class QueueCapacityBoundError(Exception):
    """
    This exception gets raised when the queue is given a negative or 0 value.
    """
    pass


class QueueIsFull(Exception):
    """
    This exception is raised when the queue is full.
    """
    pass


class QueueIsEmpty(Exception):
    """
    This exception is raised when the queue is empty.
    """
    pass


class InvalidInputTuple(Exception):
    """
    This exception is raised when the tuple is not of length 2.
    """
    pass


class InvalidBoundTuple(Exception):
    """
    This exception is raised when the tuple is not a positive integer.
    """
    pass


class InputFormatError(Exception):
    """
    This exception is raised when the input for heapSort is not a list.
    """
    pass


class InputTypeError(Exception):
    """
    This exception is raised when a list of non-tuples is passed to heapSort.
    """
    pass


class InputIntegerError(Exception):
    """
    This exception is raised when the first element of a tuple is not an int.
    """
    pass


# ============================= PriorityQueue ===================================


class PriorityQueue:
    def __init__(self, capacity):
        # INSTRUCTOR COMMENT:
        # YOu should not use isinstance. Use type(object)==int instead
        if not isinstance(capacity, int):
            # INSTRUCTOR COMMENT:
            # You havent define PriorityQueueCapacityTypeError
            raise PriorityQueueCapacityTypeError("Capacity must be of type int.")
        if capacity <= 0:
            # INSTRUCTOR COMMENT:
            # You havent define PriorityQueueCapacityBoundError
            raise PriorityQueueCapacityBoundError("Capacity must be a positive integer.")

        # INSTRUCTOR COMMENT:
        # Incorrect variable name
        self.heap = []
        self.capacity = capacity
        self.currentSize = 0

    """Initializes a priority queue with the given capacity.
        Complexity: O(1).
        Args: capacity (int), the maximum number of elements that can be stored.
        Raises: PriorityQueueCapacityTypeError: "Capacity must be of type int."
        PriorityQueueCapacityBoundError: "Capacity must be a positive integer"
        Instance Variables: heap: list, the list where the heap will be stored.
        capacity: int, the maximum number of elements that can be stored in the queue.
        currentSize: int, the current number of elements in the queue."""

    def insert(self, item):
        if not isinstance(item, tuple) or len(item) != 2:
            raise InvalidInputTuple("Input must be a tuple of length 2.")
        if not isinstance(item[0], int) or item[0] <= 0:
            raise InvalidBoundTuple("The first element of the tuple must be a positive integer.")
        if self.currentSize == self.capacity:
            raise QueueIsFull("The queue is full.")

        self.heap.append(item)
        self.currentSize += 1
        current = self.currentSize - 1
        parent = (current - 1) // 2

        # INSTRUCTOR COMMENT
        #   Incorrect while loop
        #   It should be:
        #       self.heap[parent][0] < self.heap[current][0]
        #   The while loop continue to run until parent < current(child)

        while parent >= 0 and self.heap[parent][0] > self.heap[current][0]:
            self.heap[parent], self.heap[current] = self.heap[current], self.heap[parent]
            current = parent
            parent = (current - 1) // 2

        return True

    """Adds a tuple to the queue based on its priority, returns true if it was successful.
       Complexity: O(lg(n).
       Args: item: a tuple containing priority and item (priority, item), where priority 
       is a positive integer (0 < priority <= infinity) and item is any Python object.
       Returns:
       True if the insertion was successful, false otherwise.
       Raises:
       QueueIsFull: if the queue is already full and the insertion cannot be performed.
       InvalidInputTuple: if the input tuple is not of length 2.
       InvalidBoundTuple: if the input is not a positive integer."""

    def extractMax(self):
        if self.currentSize == 0:
            raise QueueIsEmpty("The queue is empty.")

        max_item = self.heap[0]
        self.heap[0] = self.heap[self.currentSize - 1]
        self.currentSize -= 1
        self.heap.pop()
        self.maxHeapify(0)
        return max_item

    """Extracts and returns the tuple with the highest priority from the priority queue.
       Complexity: O(log(n))
       Returns:
       Tuple: the tuple with the highest priority.
       Raises:
       QueueIsEmpty: if the queue is empty and there is no item to extract."""

    def maxHeapify(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < self.currentSize and self.heap[left][0] > self.heap[largest][0]:
            largest = left
        if right < self.currentSize and self.heap[right][0] > self.heap[largest][0]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.maxHeapify(largest)

    """Maintains the max-heap property of the priority queue.
        Args:
        i (int): the index of the node to be put on the heap.
        Returns:
        None
        Complexity: O(log(n))"""

    def peekMax(self):
        if self.currentSize > 0:
            return self.heap[0]
        else:
            # INSTRUCTOR COMMENT
            # peekMax should return False and not raise any exception
            raise QueueIsEmpty("The queue is empty.")

    """Returns the tuple with the highest priority in the queue, or False if the queue is empty.
       Returns:
       Tuple or False: the tuple with the highest priority, or False if the queue is empty.
       Complexity: O(1)"""

    def isEmpty(self):
        return self.currentSize == 0

    """Returns True if the priority queue is empty, False otherwise.
       Returns:
       bool: True if the priority queue is empty, False otherwise.
       Complexity: O(1)"""

    def isFull(self):
        return self.currentSize == self.capacity

    """Returns True if the priority queue is full, False otherwise.
       Returns:
       bool: True if the priority queue is full, False otherwise.
       Complexity: O(1)"""

    # ==============================HeapSort=========================================
    def buildMaxHeap(self):
        self.currentSize = len(self.heap)
        for i in range(self.currentSize // 2 - 1, -1, -1):
            self.maxHeapify(i)

    """This method sets the currentSize instance variable to the length of 
       the heap list (it builds the max heap from scratch). A loop iterates
       through the nodes in the list, starting from the parent node and working
       down to the root. MaxHeapify is called for each node to ensure it's 
       placed correctly."""

    def heapSort(self, lst):
        if type(lst) != list:
            # INSTRUCTOR COMMENT:
            # It must be InputError

            raise InputFormatError("Input must be a list.")
        # INSTRUCTOR COMMENT:
        # Variable name "i" is confusing. Use something more meaningful like "item"
        for i in lst:
            if not isinstance(i, tuple):
                raise InputTypeError("Each item in the list must be a tuple.")
            if len(i) != 2:
                raise InvalidInputTuple("Each tuple must have exactly two elements.")
            if not isinstance(i[0], int):
                raise InputIntegerError("The first element in the tuple must be an integer.")
            if i[0] <= 0:
                raise InvalidBoundTuple("The priority must be a positive integer.")

        self.heap = lst
        self.currentSize = len(lst)
        self.buildMaxHeap()

        for i in range(len(lst) - 1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.currentSize -= 1
            self.maxHeapify(0)

        return self.heap

    """Sorts the given list of tuples using the heap data structure.
       Parameters:
       lst (list): A list of tuples (priority, item).
       Returns:
       list: The sorted list of tuples.
       Raises:
       InputFormatError: If the input is not a list.
       InputTypeError: If the input is not made of tuples.
       InputIntegerError: If the first element is not an integer.
       InvalidBoundError: If the priority is not positive.
       Complexity:
       O(nlg(n))"""


if __name__ == '__main__':
    q = PriorityQueue(10)
    print(q.peekMax())