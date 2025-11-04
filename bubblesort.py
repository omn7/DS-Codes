def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage
salaries = [57000.0, 88000.5, 43000.75, 120000.0, 64000.0, 91000.0]
bubble_sort(salaries)
print("Sorted salaries:", salaries)
print("Top 5 highest salaries:", salaries[-5:])
