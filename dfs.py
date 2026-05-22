"this is an implementation of depth first search for both graph and tree data structures"
def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited=set()
    
    visited.add(start)
    result=[start]
    
    for neighbor in graph.get(start,[]):
        if neighbor not in visited:
            result.extend(dfs_recursive(graph,neighbor, visited)) 
    return result

class TreeNode:
    def __init__(self, val, left= None, right=None):
        self.val=val
        self.left=left
        self.right=right

def dfs_inorder(node):
    if not node:
        return []
    return dfs_inorder(node.left)+[node.val]+dfs_inorder(node.right)

def dfs_preorder(node):
    if not node:
        return []
    return [node.val]+dfs_preorder(node.left)+dfs_preorder(node.right)

def dfs_postorder(node):
    if not node:
        return []
    return dfs_postorder(node.left)+dfs_postorder(node.right)+[node.val]

if __name__ == "__main__":
    graph={'A': ['B', 'C'], 'B': ['D'], 'C': ['E'], 'D': [], 'E':[]}
    print("DFS:", dfs_recursive(graph,'A'))
    
    root=TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print("In-order:", dfs_inorder(root))
    print("Pre-order:", dfs_preorder(root))
    print("Post-order:", dfs_postorder(root))
