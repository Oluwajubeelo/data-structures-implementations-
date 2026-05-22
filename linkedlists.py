class Node:
    "A single node in a linked list."
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    "The linked list manager."
    def __init__(self):
        self.head = None

    def append(self, data):
        "Adds a new node to the end of the list."
        new_node = Node(data)
        

        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
            
        current.next = new_node

    def prepend(self, data):
        "Adds a new node to the beginning of the list."
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        "Deletes the first node containing the specified data."
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return


        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next:
            current.next = current.next.next

    def display(self):
        "Prints the list in a readable format."
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        
        elements.append("None")
        print(" -> ".join(elements))

if __name__ == "__main__":
    ll = LinkedList()
    
    ll.append(10)
    ll.append(20)
    ll.append(30)
    
    print("After appending:")
    ll.display()
    
    ll.prepend(5)
    print("After prepending 5:")
    ll.display() 
    
    ll.delete(20)
    print("After deleting 20:")
    ll.display()