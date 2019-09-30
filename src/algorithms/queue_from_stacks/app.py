class QueueFromStacks:
    """
    Source : Implement Queue using Stacks

    Implement the following operations of a queue using stacks.

    push(x) -- Push element x to the back of queue.
    pop() -- Removes the element from in front of queue.
    peek() -- Get the front element.
    empty() -- Return whether the queue is empty.
    Example:

    MyQueue queue = new MyQueue();

    queue.push(1);
    queue.push(2);
    queue.peek();  // returns 1
    queue.pop();   // returns 1
    queue.empty(); // returns false
    Notes:

    You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
    Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
    You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dequeue_stack = []
        self.enqueue_stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.__move_to_enqueue_stack()

        self.enqueue_stack.append(x)  # push to top

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.__move_to_dequeue_stack()

        return self.dequeue_stack.pop()  # pop from top

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
            return None

        self.__move_to_dequeue_stack()

        return self.dequeue_stack[-1]  # peek

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.dequeue_stack and not self.enqueue_stack

    def __move_to_dequeue_stack(self) -> None:
        while self.enqueue_stack:
            self.dequeue_stack.append(self.enqueue_stack.pop())

    def __move_to_enqueue_stack(self) -> None:
        while self.dequeue_stack:
            self.enqueue_stack.append(self.dequeue_stack.pop())
