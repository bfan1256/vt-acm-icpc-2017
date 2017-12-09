def jump_search(arr, x):
    import math
    n = len(arr)
    step = math.floor(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < x:
        prev = step
        step += math.floor(math.sqrt(n))
        if prev >= n:
            return -1

    while arr[prev] < x:
        prev = prev + 1
        if prev == min(step, n):
            return -1
    if arr[prev] == x:
        return prev
    return -1


def linear_search(sequence, target):
    for index, item in enumerate(sequence):
        if item == target:
            return index
    return None


def binary_search(sorted_collection, item):
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        midpoint = (left + right) // 2
        current_item = sorted_collection[midpoint]
        if current_item == item:
            return midpoint
        else:
            if item < current_item:
                right = midpoint - 1
            else:
                left = midpoint + 1
    return None


def interpolation_search(sorted_collection, item):
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        point = left + ((item - sorted_collection[left]) * (right - left)) // (
            sorted_collection[right] - sorted_collection[left])

        #out of range check
        if point < 0 or point >= len(sorted_collection):
            return None

        current_item = sorted_collection[point]
        if current_item == item:
            return point
        else:
            if item < current_item:
                right = point - 1
            else:
                left = point + 1
    return None
