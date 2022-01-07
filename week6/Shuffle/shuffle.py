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
print(shuffle(sampleInput ))

# Time Complexity should be O(n)