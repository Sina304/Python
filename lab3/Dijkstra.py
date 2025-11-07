### ZŁOŻONOŚĆ O(V^2)


graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'B': 1, 'D': 8},
    'D': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}  #ustawiamy wszystkie dystanse na niesk.
    distances[start] = 0                                #ale start na 0
    previous = {node: None for node in graph}           #lista poprzednich 
    visited = set()                                     #odwiedzone
    #bedzie to dzialalo dopóty, dopóki nie zaliczymy wszystkich nodów
    while len(visited) < len(graph):                    
        current_node = min(                           #wybieramy nieodwiedzony wierzcholek
            (node for node in graph if node not in visited),    #ktory jest najblizej
            key=lambda node: distances[node]
        )
        
        visited.add(current_node)                               #od razu dodajemy do odwiedzonych
        
        for neighbor, cost in graph[current_node].items():      
            new_distance = distances[current_node] + cost       #dystans potencjalny
            if new_distance < distances[neighbor]:              #jezeli jest lepszy to:
                distances[neighbor] = new_distance              #podmieniamy
                previous[neighbor] = current_node               #i dopisujemy jaki byl jego poprzednik
    
    return distances, previous

def get_path(previous, target):   #tu wsm ten start niep
    path = []
    current = target
    
    while current is not None:
        path.append(current)            #drogie po prostu bierzemy od konca i idziemy po poprzednikach
        path.append("-->")
        current = previous[current]
    
    path.pop()              #usuniecie nadmiarowej strzalki
    path.reverse()          #odwrocenie
    return path


distances, previous = dijkstra(graph, 'A')
print(distances)
print(get_path(previous, 'D'))