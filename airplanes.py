def min_planes_to_reach_last_airport(arr):
    n = len(arr)
    if n == 0:
        return -1
    
    planes_needed = 0
    current_fuel = arr[0]
    max_reachable = arr[0]
    
    for i in range(1, n):
        if i > max_reachable:
            return -1  # Unable to reach the current airport
        
        max_reachable = max(max_reachable, i + arr[i])
        
        if i > current_fuel:
            planes_needed += 1
            current_fuel = max_reachable
    
    return planes_needed + 1  # Add 1 for the last airport

# Example usage:
arr1 = [2, 1, 2, 3, 1]
arr2 = [1, 6, 3, 4, 5, 0, 0, 0, 6]
arr3 = [3, 2, 1, 0, 4]
print(min_planes_to_reach_last_airport(arr1))  # Output: 2
print(min_planes_to_reach_last_airport(arr2))  # Output: 3
print(min_planes_to_reach_last_airport(arr3))  # Output: -1
