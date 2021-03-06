# Iteration
def loop1():
    odd_sum = 0
    for i in range(20):
        if (i % 2) == 1:
            odd_sum += i
    print(odd_sum)
    return odd_sum
loop1()

def loop2():
    i = 0
    even_sum = 0
    while i < 20:
        if (i % 2) == 0:
            even_sum += i
        i += 1
    print(even_sum)
    return even_sum
loop2()

# Recursion
def loop1Rec(num=20, odd_sum=0):
    if num <= 1:
        odd_sum += num
        return odd_sum
    elif num % 2 == 1:
        odd_sum += num
    return loop1Rec(num-1, odd_sum)
print(loop1Rec())

def loop2Rec(num=0, even_sum=0):
    if num >= 20:
        return even_sum
    elif num % 2 == 0:
        even_sum += num
    return loop2Rec(num+1, even_sum)
print(loop2Rec())