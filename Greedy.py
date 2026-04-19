from Input_Modeling import parcels, max_capacity

def greedy_selection(parcels, capacity):
    parcels.sort(key=lambda x: x['value']/x['weight'], reverse=True)
    
    selected = []
    total_weight = 0
    
    for p in parcels:
        if total_weight + p['weight'] <= capacity:
            selected.append(p)
            total_weight += p['weight']
    
    return selected

print("Selected Parcels:", greedy_selection(parcels, max_capacity))