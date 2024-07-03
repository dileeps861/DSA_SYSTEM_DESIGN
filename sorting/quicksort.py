"""
Quick Sort:

Also uses divide-and-conquer
In-place sorting (though this implementation creates new lists for simplicity)
Average time complexity: O(n log n)
Worst-case time complexity: O(n^2) (rare with good pivot selection)
Space complexity: O(log n) average case due to recursion stack
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = quick_sort(arr)
print(sorted_arr)
