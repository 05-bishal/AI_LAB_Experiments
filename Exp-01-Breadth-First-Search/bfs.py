from collections import deque

def bfs(graph, start):
    """
    Breadth First Search (BFS) Traversal
    Explores neighbor nodes first before moving to next depth level using a Queue (FIFO).
    """
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    traversal_order = []
    print("BFS Traversal Order:")

    while queue:
        node = queue.popleft()
        traversal_order.append(node)
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    print()
    return traversal_order


if __name__ == "__main__":
    # Graph Representation (Adjacency List)
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['G'],
        'F': [],
        'G': []
    }

    print("Graph Adjacency List:")
    for node, neighbors in graph.items():
        print(f"  {node} -> {neighbors}")
    print()

    start_node = 'A'
    print(f"Starting BFS from node '{start_node}':")
    bfs(graph, start_node)
