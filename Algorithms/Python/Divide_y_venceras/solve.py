def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_part = array[:mid]
    right_part = array[mid:]

    sorted_left = merge_sort(left_part)
    sorted_right = merge_sort(right_part)

    return combine(sorted_left, sorted_right)

def combine(left_part, right_part):
    result = []
    i = 0
    j = 0

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            result.append(left_part[i])
            i += 1
        else:
            result.append(right_part[j])
            j += 1

    while i < len(left_part):
        result.append(left_part[i])
        i += 1

    while j < len(right_part):
        result.append(right_part[j])
        j += 1

    return result