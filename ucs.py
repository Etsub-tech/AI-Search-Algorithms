import heapq

def uniform_cost_search(graph, start, goal):

    pq = [(0, start, [start])]

    visited = {}

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node == goal:
            return path, cost

        if node in visited and visited[node] <= cost:
            continue

        visited[node] = cost

        for neighbor, edge_cost in graph[node]:
            new_cost = cost + edge_cost
            new_path = path + [neighbor]

            heapq.heappush(pq, (new_cost, neighbor, new_path))

    return None, float('inf')

