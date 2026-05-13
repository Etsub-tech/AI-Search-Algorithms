from graph import graph
from bfs import bfs
from dfs import dfs
from ucs import uniform_cost_search


def print_separator():
    print("=" * 50)


def print_result(algorithm, path, extra, extra_label="Expansion Order"):
    print(f"\n  Path Found : {' -> '.join(path) if path else 'No path found'}")
    if isinstance(extra, list):
        print(f"  {extra_label}: {' -> '.join(extra)}")
    else:
        print(f"  {extra_label}: {extra}")


def display_graph():
    print("\n  Graph Structure:")
    for node in sorted(graph):
        neighbors = ', '.join(f"{n}(w:{c})" for n, c in graph[node])
        print(f"    {node} -> {neighbors}")


def get_valid_node(prompt):
    while True:
        node = input(prompt).strip().upper()
        if node in graph:
            return node
        print(f"  [!] '{node}' is not in the graph. Valid nodes: {', '.join(sorted(graph.keys()))}")


def run_all(start, goal):
    print_separator()

    # BFS
    print("\n[1] BFS — Breadth-First Search")
    path, order = bfs(graph, start, goal)
    print_result("BFS", path, order, "Expansion Order")

    print_separator()

    # DFS
    print("\n[2] DFS — Depth-First Search")
    path, order = dfs(graph, start, goal)
    print_result("DFS", path, order, "Expansion Order")

    print_separator()

    # UCS
    print("\n[3] UCS — Uniform Cost Search")
    path, cost = uniform_cost_search(graph, start, goal)
    print_result("UCS", path, f"{cost}", "Total Cost")

    print_separator()


def main():
    print_separator()
    print("   GRAPH SEARCH ALGORITHMS — MAIN PROGRAM")
    print_separator()

    while True:
        print("\n  MENU:")
        print("  [1] Show graph")
        print("  [2] Run BFS")
        print("  [3] Run DFS")
        print("  [4] Run UCS")
        print("  [5] Run ALL algorithms")
        print("  [6] Exit")

        choice = input("\n  Enter your choice (1-6): ").strip()

        if choice == '1':
            display_graph()

        elif choice in ('2', '3', '4', '5'):
            print()
            start = get_valid_node("  Enter Start Node: ")
            goal  = get_valid_node("  Enter Goal Node : ")
            print(f"\n  Searching from '{start}' to '{goal}'...")

            if choice == '2':
                print_separator()
                print("\n[BFS] Breadth-First Search")
                path, order = bfs(graph, start, goal)
                print_result("BFS", path, order, "Expansion Order")
                print_separator()

            elif choice == '3':
                print_separator()
                print("\n[DFS] Depth-First Search")
                path, order = dfs(graph, start, goal)
                print_result("DFS", path, order, "Expansion Order")
                print_separator()

            elif choice == '4':
                print_separator()
                print("\n[UCS] Uniform Cost Search")
                path, cost = uniform_cost_search(graph, start, goal)
                print_result("UCS", path, f"{cost}", "Total Cost")
                print_separator()

            elif choice == '5':
                run_all(start, goal)

        elif choice == '6':
            print("\n  Goodbye!\n")
            break

        else:
            print("  [!] Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()