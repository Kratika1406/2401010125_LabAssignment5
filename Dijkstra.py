import heapq
from Input_Modeling import graph   # make sure file exists

def dijkstra(graph, start):
    pq = [(0, start)]
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    
    while pq:
        d, node = heapq.heappop(pq)
        
        # ⚠️ Important fix (avoid outdated values)
        if d > dist[node]:
            continue
        
        for neighbor, weight in graph[node].items():
            new_dist = d + weight
            
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    
    return dist

print("Shortest Paths:", dijkstra(graph, 'A'))