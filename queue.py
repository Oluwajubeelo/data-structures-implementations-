"""
CSC 341 - Data Structures
Queue Implementation
"""

from collections import deque
from typing import Any, Optional

class Queue:
    """A Queue implementation supporting FIFO operations."""
    def __init__(self) -> None:
        """Initializes an empty queue using double-ended queue (deque)."""
        self._items: deque[Any] = deque()

    def enqueue(self, item: Any) -> None:
        """Adds an item to the end of the queue.
        """
        self._items.append(item)

    def dequeue(self) -> Optional[Any]:
        """Removes and returns the item at the front of the queue. Returns None if empty.
        """
        if self.is_empty():
            return None
        return self._items.popleft()

    def peek(self) -> Optional[Any]:
        """Returns the item at the front of the queue without removing it. Returns None if empty.
        """
        if self.is_empty():
            return None
        return self._items[0]

    def is_empty(self) -> bool:
        """Checks if the queue is empty.
        """
        return len(self._items) == 0

    def len(self) -> int:
        """Returns the number of items in the queue.
        """
        return len(self._items)

    def __len__(self) -> int:
        """Enables the standard python len(queue) functionality."""
        return self.len()

    def __repr__(self) -> str:
        """Returns a string representation of the queue."""
        return f"Queue({list(self._items)})"


# Driver code to demonstrate Queue operations
if __name__ == "__main__":
    q = Queue()
    print("Is queue empty?", q.is_empty())
    
    print("\nEnqueueing items: 10, 20, 30")
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("Queue:", q)
    print("Queue Length:", len(q))
    
    print("\nPeek front item:", q.peek())
    
    print("\nDequeueing item:", q.dequeue())
    print("Queue after dequeue:", q)
    
    print("\nDequeueing remaining items...")
    q.dequeue()
    q.dequeue()
    print("Is queue empty now?", q.is_empty())