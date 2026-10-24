def dfs(graph, node, visited, traversal_order=None):
    """
    Depth First Search (DFS) Traversal using Recursion
    Explores as far as possible along each branch before backtracking using Stack (LIFO).
    """
    if traversal_order is None:
        traversal_order = []

    visited.add(node)
    traversal_order.append(node)
    print(node, end=" ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited, traversal_order)

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

    visited = set()
    start_node = 'A'
    print(f"Starting DFS from node '{start_node}':")
    print("DFS Traversal Order:")
    dfs(graph, start_node, visited)
    print()
