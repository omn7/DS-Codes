"""Explanation: Binary search works only on sorted lists.
It repeatedly divides the search interval in half, comparing the middle 
element with the target. If the middle element is equal to the target, 
search ends. Otherwise, it decides which half of the list to search next,
effectively reducing search time exponentially compared to linear search."""

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example usage
accounts = [101, 205, 320, 405, 512]
target_id = 205
index = binary_search(accounts, target_id)
print("Account found at index:" if index != -1 else "Account not found", index)
