class Node:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
    def __repr__(self):
        return f"Node({self.value})"

class BST:
    def __init__(self):
        self.root=None
        self.left_array=[]
        self.right_array=[]
    def insert(self, value):
        if self.root==None:
            self.root=Node(value)
            return
        self._insert_recursive(self.root, value)
    def _insert_recursive(self, node, value):
        if value<node.value:
            if node.left==None:
                node.left=Node(value)
                self.left_array.append(node.left)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right==None:
                node.right=Node(value)
                self.right_array.append(node.right)
            else:
                self._insert_recursive(node.right, value)
    def inorder_list(self):
        result=[]
        def _in(node):
            if not node:
                return
            _in(node.left)
            result.append(node.value)
            _in(node.right)
        _in(self.root)
        return result
    def preorder_list(self):
        result=[]
        def _pre(node):
            if not node:
                return
            result.append(node.value)
            _pre(node.left)
            _pre(node.right)
        _pre(self.root)
        return result
    def postorder_list(self):
        result=[]
        def _post(node):
            if not node:
                return
            _post(node.left)
            _post(node.right)
            result.append(node.value)
        _post(self.root)
        return result

array=[20,4,50,25,45,60]
bst=BST()
for num in array:
    bst.insert(num)

print("Root:", bst.root)
print("Left Array:", bst.left_array)
print('Right array',bst.right_array)

print("Bst Inorder List:", bst.inorder_list())
print("Bst Preorder List:", bst.preorder_list())
print("Bst Postorder List:", bst.postorder_list())

