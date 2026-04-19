from Input_Modeling import graph

def tsp_recursive(graph, current, visited):
    if len(visited) == len(graph):
        return graph[current]['A']  # return to start
    
    min_cost = float('inf')
    
    for neighbor in graph[current]:
        if neighbor not in visited:
            cost = graph[current][neighbor] + tsp_recursive(graph, neighbor, visited | {neighbor})
            min_cost = min(min_cost, cost)
    
    return min_cost

print("Minimum Route Cost:", tsp_recursive(graph, 'A', {'A'}))