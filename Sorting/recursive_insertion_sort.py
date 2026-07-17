def insertion_sort(arr, i, n):
    if i == n:
        return
    j = i
    while j > 0 and arr[j - 1] > arr[j]:
        arr[j - 1], arr[j] = arr[j], arr[j - 1]
        j -= 1
    insertion_sort(arr, i + 1, n)

arr = [13, 46, 24, 52, 20, 9]
n = len(arr)
print("Before Using Insertion Sort:")
print(arr)
insertion_sort(arr, 0, n)
print("After Using Insertion Sort:")
print(arr)
