# Lab 6 - Part 4: Implement the graph in Python and traverse it with DFS

# The tree from the diagram, stored as an adjacency list (dictionary)
graph = {
    1: [2, 7, 8],
    2: [3, 6],
    3: [4, 5],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [9, 12],
    9: [10, 11],
    10: [],
    11: [],
    12: [],
}


"""DFS using an explicit stack (follows the iterative pseudocode)."""
def dfs_iterative(graph, start):
    visited = set()
    order = []
    stack = [start]

    visited.add(start)
    while stack:
        node = stack.pop()   # removes and returns the top item
        order.append(node)
        # push neighbours in reverse so the leftmost child is popped first
        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append(neighbour)
                visited.add(neighbour)
    return order



"""DFS using recursion (follows the recursive pseudocode)."""
def dfs_recursive(graph, node, visited=None, order=None):
    if visited is None:
        visited = set()
        order = []
    visited.add(node)
    order.append(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs_recursive(graph, neighbour, visited, order)
    return order

print("Adjacency list:")    
for node, neighbours in graph.items():
    print(f"  {node} -> {neighbours}")

print("\nDFS (iterative, stack):", dfs_iterative(graph, 1))
print("DFS (recursive):       ", dfs_recursive(graph, 1))


# -----------------------------------------------------------------------------------------------------------

# Lab 6 - Part 5: Walkthrough task
# Python version of the C++ DFS program (directed graph, adjacency list, recursive DFS)


class Graph:
    """Directed graph using an adjacency list representation."""

    def __init__(self, V):
        self.V = V                                # number of vertices
        self.adj = [[] for _ in range(V)]         # adj[v] = list of v's neighbours

    def add_edge(self, v, w):
        """Add an edge from v to w (directed, so only v's list changes)."""
        self.adj[v].append(w)

    def _dfs_util(self, v, visited):
        """Recursive helper: mark v as visited, print it, recurse on neighbours."""
        visited[v] = True
        print(v, end=" ")

        for neighbour in self.adj[v]:
            if not visited[neighbour]:
                self._dfs_util(neighbour, visited)

    def dfs(self, v):
        """DFS traversal of the vertices reachable from v."""
        # Mark all the vertices as not visited
        visited = [False] * self.V
        # Call the recursive helper function to print the DFS traversal
        self._dfs_util(v, visited)


if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Following is Depth First Traversal (starting from vertex 2)")
    g.dfs(2)
    print()



# -----------------------------------------------------------------------------------------------------------
# Lab 6 - Part 6: Practice Task 1
# Implement the tree (start node A, goal node G) and search it with
# Depth First Search using a Stack.

# The tree from the diagram as an adjacency list.
# Children are listed left to right, as drawn in the diagram.
graph = {
    "A": ["B", "F", "D", "E"],
    "B": ["K", "J"],
    "K": ["N", "M"],
    "J": [],
    "N": [],
    "M": [],
    "F": [],
    "D": ["G"],
    "G": [],
    "E": ["C", "H", "I"],
    "C": [],
    "H": [],
    "I": ["L"],
    "L": [],
}


def dfs_stack(graph, start, goal):
    """DFS using an explicit stack. Stops as soon as the goal is reached.

    Returns (visit_order, path_to_goal). path_to_goal is None if the goal
    cannot be reached.
    """
    visited = set()
    order = []
    parent = {start: None}       # remembers how we reached each node (for the path)
    stack = [start]              # list used as a stack: append = push, pop = pop

    while stack:
        node = stack.pop()       # take the most recently added node
        if node in visited:
            continue
        visited.add(node)
        order.append(node)

        if node == goal:         # goal test
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return order, path[::-1]

        # push children in reverse so the leftmost child is popped first
        for child in reversed(graph[node]):
            if child not in visited:
                parent[child] = node
                stack.append(child)

    return order, None


if __name__ == "__main__":
    print("Adjacency list:")
    for node, children in graph.items():
        print(f"  {node} -> {children}")

    start, goal = "A", "G"
    order, path = dfs_stack(graph, start, goal)

    print(f"\nDFS using stack (start = {start}, goal = {goal})")
    print("Nodes visited in order:", " -> ".join(order))
    if path:
        print("Goal found!")
        print("Path from start to goal:", " -> ".join(path))
    else:
        print("Goal not found.")