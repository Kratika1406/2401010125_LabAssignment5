# Graph (distance between locations)
graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

# Parcel data
parcels = [
    {"id": 1, "value": 100, "weight": 5, "time": (1, 5)},
    {"id": 2, "value": 60, "weight": 3, "time": (2, 6)},
    {"id": 3, "value": 120, "weight": 8, "time": (3, 7)}
]

# Vehicle capacity
max_capacity = 10