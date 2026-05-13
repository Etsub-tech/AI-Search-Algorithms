#Depth First Search Algorithm

def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    expansion_order = []

    while stack:
        current_node, path = stack.pop()

        if current_node not in visited:
            visited.add(current_node)
            expansion_order.append(current_node)

            if current_node == goal:
                return path, expansion_order

            for neighbour, cost in reversed(graph[current_node]):
                if neighbour not in visited:
                    stack.append((neighbour, path + [neighbour]))

    return None, expansion_order

