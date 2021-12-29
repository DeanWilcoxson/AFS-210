def recursive_binary_search(list, value):
    while len(list) != 0:
        midway = len(list)//2
        if list[midway] == value:
            return True
        elif list[midway] > value:
            return recursive_binary_search(list, value)
        elif list[midway] < value:
            return recursive_binary_search(list, value)
        else:
            return False


# def iterative_binary_search(list, value):
#     start, end = 0, len(list) - 1
#     while start <= end:
#         mid = (start + end)//2


sampleInput1 = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
sampleInput2 = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
sampleInput3 = ["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"]

recursive_binary_search(sampleInput1, 31)
recursive_binary_search(sampleInput2, 77)
# recursive_binary_search(sampleInput3, "Delta")
