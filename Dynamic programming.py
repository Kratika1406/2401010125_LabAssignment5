from Input_Modeling import parcels

def check_time_windows(parcels):
    valid = []
    current_time = 0
    
    for p in sorted(parcels, key=lambda x: x['time'][0]):
        start, end = p['time']
        if current_time <= end:
            current_time = max(current_time, start)
            valid.append(p)
    
    return valid

print("Valid Deliveries:", check_time_windows(parcels))