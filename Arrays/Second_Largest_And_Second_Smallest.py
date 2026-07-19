def getSecondOrderElements(n: int, a: [int]) -> [int]:

    largest = a[0]
    s_largest = float('-inf')

    smallest = a[0]
    s_smallest = float('inf')

    for i in range(len(a)):
        if a[i] > largest:
            s_largest = largest
            largest = a[i]
        elif a[i] != largest and a[i] > s_largest:
            s_largest = a[i]

    for i in range(len(a)):
        if a[i] < smallest:
            s_smallest = smallest
            smallest = a[i]
        elif a[i] != smallest and a[i] < s_smallest:
            s_smallest = a[i]

    return [s_largest, s_smallest]
