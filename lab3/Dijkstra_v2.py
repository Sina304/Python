import heapq

### ZŁOŻONOŚĆ O(E log V)

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'B': 1, 'D': 8},
    'D': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}      #ustawiamy wszystkie dystanse na nieskonczonosc
    distances[start] = 0                                    #ale zmieniamy startowy na zero wiec start=0 reszta to nieskonczonosc
    previous = {node: None for node in graph}               #tworzymy poprzednie wezly po ktorych chodzimy (narazie nie wiemy jakie)

    #kolejka priorytetowa (koszt, wierchołek), zaczynamy od startu z kosztem 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)  #wyciąga najmniejszy element z kolejki, za pierwszym razem nie ma wsm wyboru          

        # jeżeli mamy już lepszy wynik -> ignorujemy
        if current_distance > distances[current_node]:      #jezeli znamy juz lepszy wynik jak dostac sie to tego wiercholka to pomijamy (optymalizacja)
            continue

        # relaksacja sąsiadów
        for neighbor, cost in graph[current_node].items():
            new_distance = current_distance + cost          #przy pierwszym podejsciu to bedzie 0+4=4 
            if new_distance < distances[neighbor]:          #i bedzie to mniejsze niz nieskonczonosc dla B
                distances[neighbor] = new_distance          #wiec nowym dystansem dla B bedzie to 4
                previous[neighbor] = current_node           #no i z racji ze bedziemy analizowac nastepne to dodajemy ze przed B byl wlasnie A
                heapq.heappush(pq, (new_distance, neighbor))#no i pushujemy do kolejki priorytetowej dystans do B i sam B

    return distances, previous

def get_path(previous, start, target):
    path = []
    current = target
    
    while current is not None:
        path.append(current)
        current = previous[current]
        path.append("-->")
    
    path.pop()
    path.reverse()
    return path

distances, previous = dijkstra(graph, 'A')
print(distances)
print(get_path(previous, 'A', 'D'))
