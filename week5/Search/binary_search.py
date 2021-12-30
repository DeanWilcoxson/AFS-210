def recursive_BS(list, value, start=0, end=None):
    if end is None:
        end = len(list) - 1
    if start > end:
        return False

    mid = (start + end) // 2
    if value == list[mid]:
        return True
    if value < list[mid]:
        return recursive_BS(list, value, start, mid-1)
    # value > list[mid]
    return recursive_BS(list, value, mid+1, end)


def iterative_BS(list, value):
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

# print(recursive_BS(sampleInput1, 31))
# print(recursive_BS(sampleInput2, 77))
# print(recursive_BS(sampleInput3, "Delta"))

print(iterative_BS(sampleInput1, 31))
print(iterative_BS(sampleInput2, 77))
print(iterative_BS(sampleInput3, "Delta"))
