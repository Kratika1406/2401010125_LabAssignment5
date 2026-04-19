from itertools import permutations
from Input_Modeling import graph   

def tsp_bruteforce(graph):
    nodes = list(graph.keys())
    start = nodes[0]
    nodes.remove(start)
    
    min_path = None
    min_cost = float('inf')
    
    for perm in permutations(nodes):
        cost = 0
        current = start
        
        for node in perm:
            cost += graph[current][node]
            current = node
        
        cost += graph[current][start]
        
        if cost < min_cost:
            min_cost = cost
            min_path = (start,) + perm + (start,)
    
    return min_path, min_cost

print("Optimal Route:", tsp_bruteforce(graph))