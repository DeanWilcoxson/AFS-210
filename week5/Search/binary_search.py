def binary_search_recursive(list, value, start=0, end=None):
    if end is None:
        end = len(list) - 1
    if start > end:
        return False

    mid = (start + end) // 2
    if value == list[mid]:
        return True
    if value < list[mid]:
        return binary_search_recursive(list, value, start, mid-1)
    # value > list[mid]
    return binary_search_recursive(list, value, mid+1, end)


def binary_search_iterative(list, value):
    start, end = 0, (len(list) - 1)
    while start <= end:
        mid = (start + end) // 2
        if value == list[mid]:
            return True
        if value < list[mid]:
            end = mid - 1
        else:  # value > list[mid]
            start = mid + 1

    return False


sampleInput1 = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
sampleInput2 = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
sampleInput3 = ["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"]

# print(binary_search_recursive(sampleInput1, 31))
# print(binary_search_recursive(sampleInput2, 77))
# print(binary_search_recursive(sampleInput3, "Delta"))

print(binary_search_iterative(sampleInput1, 31))
print(binary_search_iterative(sampleInput2, 77))
print(binary_search_iterative(sampleInput3, "Delta"))
