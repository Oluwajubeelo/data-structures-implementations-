class MyArray:
    def __init__(self):
        self.arr = []

    def insert(self, value):
        self.arr.append(value)

    def insert_at(self, index, value):
        if index >= 0 and index <= len(self.arr):
            self.arr.insert(index, value)
        else:
            print("Invalid index")

    def delete(self, value):
        if value in self.arr:
            self.arr.remove(value)
        else:
            print("Element not found")

    def delete_at(self, index):
        if index >= 0 and index < len(self.arr):
            self.arr.pop(index)
        else:
            print("Invalid index")

    def search(self, value):
        if value in self.arr:
            print(f"{value} found at index {self.arr.index(value)}")
        else:
            print("Element not found")

    def display(self):
        print(self.arr)


a = MyArray()

a.insert(10)
a.insert(20)
a.insert(30)

a.insert_at(1, 15)

a.display()

a.delete(20)

a.display()

a.delete_at(0)

a.display()

a.search(30)