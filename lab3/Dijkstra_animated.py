import networkx as nx
import matplotlib.pyplot as plt
import heapq

graph = {
    'A': {'B': 3, 'C': 5, 'D': 4},
    'B': {'A': 3, 'E': 2, 'D': 3, 'G': 7},
    'C': {'A': 5, 'D': 2, 'G': 2},
    'D': {'A': 4, 'C': 2, 'B': 3, 'E': 5},
    'E': {'B': 2, 'D': 5, 'F': 6},
    'F': {'E': 6, 'G': 11},
    'G': {'C': 2, 'B': 7, 'F': 11}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}

    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue

        for neighbor, cost in graph[current_node].items():
            new_distance = current_distance + cost
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (new_distance, neighbor))

    return distances, previous

def get_path(previous, target):
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    return path

# --- Uruchomienie Dijkstry ---
distances, previous = dijkstra(graph, 'A')
path = get_path(previous, 'F')
print("Najkrótsze odległości:", distances)
print("Najkrótsza trasa z A do F:", path)

# --- Rysowanie grafu ---
G = nx.Graph()
for node, edges in graph.items():
    for neighbor, weight in edges.items():
        G.add_edge(node, neighbor, weight=weight)

pos = nx.spring_layout(G, seed=42)  # ładny układ

# rysowanie wszystkich węzłów i krawędzi
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1000)
nx.draw_networkx_edges(G, pos)
labels = nx.get_edge_attributes(G, 'weight')

# podświetlenie najkrótszej ścieżki
path_edges = list(zip(path, path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)

nx.draw_networkx_edge_labels(G, pos, edge_labels=labels) 

plt.title(f"Najkrótsza trasa z A do F: {' -> '.join(path)}")
plt.show()