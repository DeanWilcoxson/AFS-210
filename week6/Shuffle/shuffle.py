import random
def shuffle(list, n):
    if len(list) <= 0:
        return None
    elif len(list) < 2 and len(list) > 0:
        return list
    elif len(list) >= 2:
        for index in range(n-1,0,-1):
            randIndex = random.randint(0, index+1)
            list[index],list[randIndex] = list[randIndex],list[index]
        return list
        
sampleInput = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
n = len(sampleInput)
print("Before Shuffled: ")
print(sampleInput)
print("After Shuffled: ")
print(shuffle(sampleInput, n))
print(shuffle(sampleInput, n))
print(shuffle(sampleInput, n))
print(shuffle(sampleInput, n))
print(shuffle(sampleInput, n))
