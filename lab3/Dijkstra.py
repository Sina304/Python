### ZŁOŻONOŚĆ O(V^2)


graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'B': 1, 'D': 8},
    'D': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}
    visited = set()
    
    while len(visited) < len(graph):
        current_node = min(
            (node for node in graph if node not in visited),
            key=lambda node: distances[node]
        )
        
        visited.add(current_node)
        
        for neighbor, cost in graph[current_node].items():
            new_distance = distances[current_node] + cost
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_node
    
    return distances, previous

def get_path(previous, start, target):
    path = []
    current = target
    
    while current is not None:
        path.append(current)
        path.append("-->")
        current = previous[current]
    
    path.pop()
    path.reverse()
    return path


distances, previous = dijkstra(graph, 'A')
print(distances)
print(get_path(previous, 'A', 'D'))