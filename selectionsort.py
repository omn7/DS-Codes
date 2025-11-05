def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
       
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage
salaries = [57000.0, 88000.5, 43000.75, 120000.0, 64000.0, 91000.0]
selection_sort(salaries)
print("Sorted salaries:", salaries)
print("Top 5 highest salaries:", salaries[-5:])
