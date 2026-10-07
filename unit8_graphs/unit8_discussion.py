"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """
    # BFS uses a queue because the first node added should be the first processed.
    if start not in graph:
        return []

    visited = set()
    traversal_order = []
    queue = deque([start])

    # Mark the starting node as visited when added to the queue. This helps prevent the same node from being added multiple times.
    visited.add(start)
    while queue:
        current = queue.popleft()
        traversal_order.append(current)

        # Neighbors are added to the queue so they can be processed after the other nodes at the current level.
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # BFS differs from depth-first traversal in how it explores all neighboring nodes before moving to the next level,
    # unlike DFS, which follows one path as deeply as possible.
    return traversal_order

def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    print("\n=== GRAPH STRUCTURE ===")
    print("TODO: Create and display a graph.")
    # This graph is a simplified streaming recommendation network. Each node represents a song, and each edge represents
    # a relationship based on similar genres, artists, or ratings.The graph is represented using an adjacency list.
    # Each song contains a list of songs directly connected to it.
    graph = {
        "Song A": ["Song B", "Song C"],
        "Song B": ["Song A", "Song D", "Song E"],
        "Song C": ["Song A", "Song F"],
        "Song D": ["Song B", "Song E"],
        "Song E": ["Song B", "Song D", "Song F"],
        "Song F": ["Song C", "Song E"]
    }

    # Display the graph structure so the relationships are visible.
    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")
    print("TODO: Perform and explain BFS traversal.")

    start_node = "Song A"
    traversal = bfs(graph, start_node)

    print(f"Starting node: {start_node}")
    print("BFS traversal:", " -> ".join(traversal))

    # Add a new Song and connect it to Song E. This shows how the graph and traversal can change when a new relationship is added.
    graph["Song G"] = ["Song E"]
    graph["Song E"].append("Song G")

    print("\n=== UPDATED GRAPH ===")
    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")

    updated_traversal = bfs(graph, start_node)

    print("\nUpdated BFS traversal:")
    print(" -> ".join(updated_traversal))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")
    # Edge Case 1: Handle a missing start node safely
    # The bfs function safely returns an empty list instead of a KeyError.
    missing_start = "Song Z"
    missing_result = bfs(graph, missing_start)

    print(f"Missing start node ({missing_start}): {missing_result}")

    # Edge Case 2: Graph containing only one node
    # BFS visits the one node and then stops because there are no neighbors to add to the queue.
    single_node_graph = {
        "Song X": []
    }

    single_result = bfs(single_node_graph, "Song X")

    print(f"Single-node graph: {single_result}")

    # Edge Case 3: Empty graph
    # There is nothing, so BFS returns an empty list.
    empty_graph = {}

    empty_result = bfs(empty_graph, "Song A")

    print(f"Empty graph: {empty_result}")

if __name__ == "__main__":
    main()