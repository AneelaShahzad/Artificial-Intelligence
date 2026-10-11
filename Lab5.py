####1.BFS on given graph
from collections import deque

# Graph represented using adjacency list
graph = {
    0: [1, 4],
    1: [0, 4, 3, 2],
    2: [1, 3],
    3: [1, 4, 2],
    4: [0, 1, 3]
}

def bfs(graph, start):
    visited = set()
    queue = deque()

    # Add starting node to queue
    queue.append(start)
    visited.add(start)

    print("BFS Traversal:")

    while queue:
        # Remove first element from queue
        node = queue.popleft()

        print(node, end=" ")

        # Visit all neighbours
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


# Start BFS from node 0
bfs(graph, 0)


####2.BFS from A to goal G
from collections import deque

# Tree represented using adjacency list
tree = {
    'A': ['B', 'F', 'D', 'E'],
    'B': ['K', 'J'],
    'F': [],
    'D': ['G'],
    'E': ['C', 'H', 'I'],
    'K': ['N', 'M'],
    'J': [],
    'G': [],
    'C': [],
    'H': [],
    'I': ['L'],
    'N': [],
    'M': [],
    'L': []
}

def bfs(tree, start, goal):
    visited = set()
    queue = deque()

    # Add starting node
    queue.append(start)
    visited.add(start)

    print("BFS Search:")

    while queue:
        # Remove first node from queue
        current = queue.popleft()

        print(current, end=" ")

        # Check if goal is reached
        if current == goal:
            print("\nGoal G found!")
            return

        # Add unvisited neighbours
        for neighbour in tree[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    print("\nGoal not found.")


# Start BFS from A and search for G
bfs(tree, 'A', 'G')


####3.implementing priority queue
import heapq

# Create an empty priority queue
priority_queue = []

# Add elements
heapq.heappush(priority_queue, (3, "Task C"))
heapq.heappush(priority_queue, (1, "Task A"))
heapq.heappush(priority_queue, (2, "Task B"))
heapq.heappush(priority_queue, (5, "Task E"))
heapq.heappush(priority_queue, (4, "Task D"))

print("Priority Queue:")

# Remove elements according to priority
while priority_queue:
    priority, task = heapq.heappop(priority_queue)

    print("Priority:", priority, "| Task:", task)