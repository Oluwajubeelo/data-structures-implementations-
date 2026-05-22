"""
CSC 341 - Data Structures
AVL Tree (Self-Balancing Binary Search Tree) Implementation
"""

class AVLNode:
    # Represents a node in the AVL Tree.
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # Height is used to calculate the balance factor

    def __repr__(self):
        return f"AVLNode({self.value})"

class AVL:
    # AVL Tree implementation supporting self-balancing insertion.
    def __init__(self):
        self.root = None

    def _node_height(self, current_node):
        # Helper to get the height of a node. Returns 0 if node is None.
        return current_node.height if current_node else 0

    def _update_height(self, current_node):
        # Updates the height of a node based on its children's heights.
        current_node.height = 1 + max(self._node_height(current_node.left), self._node_height(current_node.right))

    def _balance(self, current_node):
        # Calculates the balance factor of a node (height of left subtree - height of right subtree).
        return self._node_height(current_node.left) - self._node_height(current_node.right)

    def _rotate_right(self, pivot):
        """Performs a right rotation around the pivot node to rebalance.
        
        This is used for Left-Left (LL) imbalance.
        """
        left_child = pivot.left
        orphan_subtree = left_child.right

        # Perform rotation
        left_child.right = pivot
        pivot.left = orphan_subtree

        # Update heights
        self._update_height(pivot)
        self._update_height(left_child)

        return left_child

    def _rotate_left(self, pivot):
        """Performs a left rotation around the pivot node to rebalance.
        
        This is used for Right-Right (RR) imbalance.
        """
        right_child = pivot.right
        orphan_subtree = right_child.left

        # Perform rotation
        right_child.left = pivot
        pivot.right = orphan_subtree

        # Update heights
        self._update_height(pivot)
        self._update_height(right_child)

        return right_child

    def insert(self, new_value):
        # Public method to insert a new value into the AVL tree.
        self.root = self._insert(self.root, new_value)

    def _insert(self, current_node, new_value):
        # Recursive helper to insert a value and balance the tree at each step.

        # 1. Perform standard BST insert
        if current_node is None:
            return AVLNode(new_value)
        if new_value < current_node.value:
            current_node.left = self._insert(current_node.left, new_value)
        else:
            current_node.right = self._insert(current_node.right, new_value)

        # 2. Update the height of this ancestor node
        self._update_height(current_node)

        # 3. Get the balance factor to check if it became unbalanced
        balance_value = self._balance(current_node)

        # 4. If unbalanced, apply the appropriate rotation(s)
        
        # Left-Left Case -> Single Right Rotation
        if balance_value > 1 and new_value < current_node.left.value:
            return self._rotate_right(current_node)
            
        # Right-Right Case -> Single Left Rotation
        if balance_value < -1 and new_value >= current_node.right.value:
            return self._rotate_left(current_node)
            
        # Left-Right Case -> Left Rotation on child, then Right Rotation on parent
        if balance_value > 1 and new_value >= current_node.left.value:
            current_node.left = self._rotate_left(current_node.left)
            return self._rotate_right(current_node)
            
        # Right-Left Case -> Right Rotation on child, then Left Rotation on parent
        if balance_value < -1 and new_value < current_node.right.value:
            current_node.right = self._rotate_right(current_node.right)
            return self._rotate_left(current_node)

        return current_node

    def inorder_list(self):
        """Returns the in-order traversal of the AVL tree as a list.
        
        In-order traversal of a BST yields sorted elements.
        """
        traversal_list = []
        def traverse_in(node):
            if not node: return
            traverse_in(node.left)
            traversal_list.append(node.value)
            traverse_in(node.right)
        traverse_in(self.root)
        return traversal_list


# Driver code to demonstrate AVL operations
if __name__ == "__main__":
    array = [20, 4, 50, 25, 45, 60]
    avl = AVL()
    for num in array:
        avl.insert(num)

    print("Root:", avl.root)
    print("Avl Inorder List:", avl.inorder_list())