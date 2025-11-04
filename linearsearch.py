"""Linear search checks each element of the list sequentially until it finds the target element. If found, it returns the position; otherwise, it indicates failure by returning -1. It is simple but inefficient for large lists since it checks every element."""
def linear_search(arr, target):
    for idx, value in enumerate(arr):
        #index is idx
        # Check each element one by one
        if value == target:
            # If found, return its index
            return idx
    # If the element is not found in the entire list, return -1
    return -1

# Example usage
accounts = [101, 205, 320, 405, 512]
target_id = 405
index = linear_search(accounts, target_id)
print("Account found at index:" if index != -1 else "Account not found", index)
