

def quartiles(set):
    set = [3, 7, 13, 20]
    min_value = min(set)
    max_value = max(set)
    for value in set:
        fraction = float(value - min_value) / (max_value - min_value)
        percentage = fraction * 100
        return(value, percentage)
