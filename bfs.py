from collections import deque

def bfs(graph, start, goal):
    queue = deque()
    queue.append((start, [start]))

    visited = set()
    order = []

    while queue:
        current, path = queue.popleft()

        if current in visited:
            continue

        visited.add(current)
        order.append(current)

        if current == goal:
            return path, order

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None, order


