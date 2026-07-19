def findSecondLargest(sequenceOfNumbers):
    largest = sequenceOfNumbers[0]
    s_largest = None

    for i in range(1, len(sequenceOfNumbers)):
        if sequenceOfNumbers[i] > largest:
            s_largest = largest
            largest = sequenceOfNumbers[i]

        elif sequenceOfNumbers[i] != largest and (s_largest is None or sequenceOfNumbers[i] > s_largest):
            s_largest = sequenceOfNumbers[i]

    if s_largest is None:
        return -1

    return s_largest
