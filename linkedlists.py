"""
CSC 341 - Data Structures
Singly Linked List Implementation
"""

class Node:
    """A single node in a linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node in the list

class LinkedList:
    """The linked list manager containing methods for insertion, deletion, and display."""
    def __init__(self):
        self.head = None  # Pointer to the first node in the list

    def append(self, data):
        """Adds a new node containing data to the end of the list.
        """
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
            
        current.next = new_node

    def prepend(self, data):
        """Adds a new node containing data to the beginning of the list.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """Deletes the first node containing the specified data.
        """
        if not self.head:
            return

        # If the head node itself holds the data to be deleted
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        # Traverse the list to find the node preceding the node to delete
        while current.next and current.next.data != data:
            current = current.next

        # If node was found, bypass it
        if current.next:
            current.next = current.next.next

    def display(self):
        """Prints the list in a readable formatted chain: data -> data -> None.
        """
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        
        elements.append("None")
        print(" -> ".join(elements))


# Driver code to demonstrate Linked List operations
if __name__ == "__main__":
    ll = LinkedList()
    
    print("After appending:")
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.display()
    
    print("After prepending 5:")
    ll.prepend(5)
    ll.display() 
    
    print("After deleting 20:")
    ll.delete(20)
    ll.display()