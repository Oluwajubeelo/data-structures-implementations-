"""
CSC 341 - Data Structures
Array Implementation
"""

class MyArray:
    def __init__(self):
        # Initializes an empty array.
        self.arr = []

    def insert(self, value):
        # Appends a new value to the end of the array.
        self.arr.append(value)

    def insert_at(self, index, value):
        # Inserts a value at a specific valid index.
        if index >= 0 and index <= len(self.arr):
            self.arr.insert(index, value)
        else:
            print("Invalid index")

    def delete(self, value):
        # Deletes the first occurrence of a value from the array.
        if value in self.arr:
            self.arr.remove(value)
        else:
            print("Element not found")

    def delete_at(self, index):
        # Deletes and removes the element at a specific index.
        if index >= 0 and index < len(self.arr):
            self.arr.pop(index)
        else:
            print("Invalid index")

    def display(self):
        # Displays the elements of the array in a readable list format.
        print(self.arr)


# Driver code to demonstrate operations
if __name__ == "__main__":
    a = MyArray()

    print("Inserting 10, 20, 30:")
    a.insert(10)
    a.insert(20)
    a.insert(30)
    a.display()

    print("\nInserting 15 at index 1:")
    a.insert_at(1, 15)
    a.display()

    print("\nDeleting value 20:")
    a.delete(20)
    a.display()

    print("\nDeleting element at index 0:")
    a.delete_at(0)
    a.display()

    print("\nSearching for value 30:")
    a.search(30)