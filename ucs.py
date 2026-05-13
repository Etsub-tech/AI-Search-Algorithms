import heapq

# Graph representation
graph = {
    'A': [('B', 3), ('C', 5), ('D', 2)],
    'B': [('A', 3), ('E', 1), ('F', 6)],
    'C': [('A', 5), ('G', 1)],
    'D': [('A', 2), ('H', 7)],
    'E': [('B', 1), ('I', 8), ('F', 2)],
    'F': [('B', 6), ('E', 2)],
    'G': [('C', 1), ('H', 3)],
    'H': [('D', 7), ('G', 3), ('I', 3)],
    'I': [('E', 8), ('H', 3)]
}

# Uniform Cost Search (UCS)
def uniform_cost_search(graph, start, goal):
    # Priority queue: (cost, current_node, path)
    pq = [(0, start, [start])]

    # Visited dictionary to store lowest cost
    visited = {}

    while pq:
        cost, node, path = heapq.heappop(pq)

        # If goal found
        if node == goal:
            return path, cost

        # Skip if already visited with lower cost
        if node in visited and visited[node] <= cost:
            continue

        visited[node] = cost

        # Explore neighbors
        for neighbor, edge_cost in graph[node]:
            new_cost = cost + edge_cost
            new_path = path + [neighbor]

            heapq.heappush(pq, (new_cost, neighbor, new_path))

    return None, float('inf')


# Example usage
start_node = 'A'
goal_node = 'I'

optimal_path, total_cost = uniform_cost_search(graph, start_node, goal_node)

# Output
print("Optimal Path:", " -> ".join(optimal_path))
print("Total Path Cost:", total_cost)