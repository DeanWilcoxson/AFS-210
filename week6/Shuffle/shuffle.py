import random
def shuffle(list):
    if len(list) <= 0:
        return None
    elif len(list) == 1:
        return list
    else:
        for index in range(len(list)-1, 0, -1):
            randIndex = random.randint(0, index)
            list[index], list[randIndex] = list[randIndex], list[index]
        return list

sampleInput = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
print("Before Shuffled: ")
print(sampleInput)
print("After Shuffled: ")
print(shuffle(sampleInput))
print(shuffle(sampleInput))
print(shuffle(sampleInput))
print(shuffle(sampleInput))
print(shuffle(sampleInput))

# Time Complexity should be O(n)


def no_Random_Shuffle(list):
    if len(list) <= 0:
        return None
    elif len(list) == 1:
        return list
    else:
        for index in range(len(list)-1, 0, -1):
            # Using equations to find different indices in the list we can compare and swap with what is in the index at the time of compareing.
            mid = len(list) // 2
            pivot = (len(list)//2)//2
            # if statement to compare and swap the index with the two values  
            if list[index] < mid:
                list[index], list[mid] = list[mid], list[index]
            elif list[index] > mid:
                list[index], list[pivot] = list[pivot], list[index]
            else:
                return None
        return list
# Time complexity should be O(n)

sampleInput = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
print("Before Shuffled: ")
print(sampleInput)
print("After Shuffled: ")
print(no_Random_Shuffle(sampleInput))
print(no_Random_Shuffle(sampleInput))
print(no_Random_Shuffle(sampleInput))
print(no_Random_Shuffle(sampleInput))
print(no_Random_Shuffle(sampleInput))