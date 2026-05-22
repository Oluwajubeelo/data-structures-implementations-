class AVLNode:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
        self.height=1

    def __repr__(self):
        return f"AVLNode({self.value})"

class AVL:
    def __init__(self):
        self.root=None
    def _node_height(self, current_node):
        return current_node.height if current_node else 0
    def _update_height(self, current_node):
        current_node.height=1+max(self._node_height(current_node.left), self._node_height(current_node.right))
    def _balance(self, current_node):
        return self._node_height(current_node.left)-self._node_height(current_node.right)
    def _rotate_right(self, pivot):
        left_child=pivot.left
        orphan_subtree=left_child.right
        left_child.right=pivot
        pivot.left=orphan_subtree
        self._update_height(pivot)
        self._update_height(left_child)
        return left_child
    def _rotate_left(self, pivot):
        right_child=pivot.right
        orphan_subtree=right_child.left
        right_child.left=pivot
        pivot.right=orphan_subtree
        self._update_height(pivot)
        self._update_height(right_child)
        return right_child
    def insert(self, new_value):
        self.root=self._insert(self.root, new_value)
    def _insert(self, current_node, new_value):
        if current_node is None:
            return AVLNode(new_value)
        if new_value<current_node.value:
            current_node.left=self._insert(current_node.left, new_value)
        else:
            current_node.right=self._insert(current_node.right, new_value)

        self._update_height(current_node)
        balance_value=self._balance(current_node)

        if balance_value>1 and new_value<current_node.left.value:
            return self._rotate_right(current_node)
        if balance_value<-1 and new_value>=current_node.right.value:
            return self._rotate_left(current_node)
        if balance_value>1 and new_value>=current_node.left.value:
            current_node.left=self._rotate_left(current_node.left)
            return self._rotate_right(current_node)
        if balance_value<-1 and new_value<current_node.right.value:
            current_node.right=self._rotate_right(current_node.right)
            return self._rotate_left(current_node)
        return current_node

    def inorder_list(self):
        traversal_list=[]
        def traverse_in(node):
            if not node: return
            traverse_in(node.left)
            traversal_list.append(node.value)
            traverse_in(node.right)
        traverse_in(self.root)
        return traversal_list

array=[20,4,50,25,45,60]
avl=AVL()
for num in array:
    avl.insert(num)

print("Root:", avl.root)
print("Avl Inorder List:", avl.inorder_list())