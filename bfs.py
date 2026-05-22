"""
CSC 341 - Data Structures
Breadth-First Search (BFS) Implementation
"""

from collections import deque

def bfs(graph, start):
    """Performs Breadth-First Search (BFS) on a graph starting from a given node.
    """
    # Use a set to track visited nodes in O(1) time
    visited = set()
    
    # Initialize a double-ended queue (deque) with the starting node
    queue = deque([start])
    visited.add(start)
    
    # Loop until there are no more nodes to explore
    while queue:
        # Pop the leftmost element (FIFO)
        node = queue.popleft()
        print(node)
        
        # Explore all unvisited neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    print("Visited nodes:", visited)

# Driver code to demonstrate BFS
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'E'],
        'D': ['B'],
        'E': ['C']
    }
    
    print("Executing BFS starting from node 'A':")
    bfs(graph, 'A')
    # hope y'all understand 😉😉