from Input_Modeling import graph

def prim(graph):
    start = list(graph.keys())[0]
    visited = set([start])
    edges = []
    
    while len(visited) < len(graph):
        min_edge = (None, None, float('inf'))
        
        for u in visited:
            for v, w in graph[u].items():
                if v not in visited and w < min_edge[2]:
                    min_edge = (u, v, w)
        
        edges.append(min_edge)
        visited.add(min_edge[1])
    
    return edges

print("Minimum Spanning Tree:", prim(graph))

