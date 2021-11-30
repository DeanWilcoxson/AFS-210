from random import randint
# Data1
print("\nData1")
data_one = (7, False, "Apple", True, 7, 98.6)


def count():
    count = 0
    for i in data_one:
        count += 1
    print("\t", count)


count()


def findFourthItem():
    count = 0
    for i in data_one:
        count += 1
        if count == 4:
            print("\t", i)


findFourthItem()


def countSeven():
    count = 0
    for i in data_one:
        if i == 7:
            count += 1
    print("\t", count)


countSeven()

# Data2
print("\nData2")
data_two = {"July", 4, 8, "Tango", 4.3, "Bingo"}


def removeRand():
    count = 0
    for i in data_two:
        count += 1
        value = randint(0, count)
        if count == value:
            data_two.remove(i)
            data_two.add("Alpha")
            break
        else:
            value += 1
    print("\t", data_two)


removeRand()

# Data3
print("\nData3")
data_three = ["A", 7, -1, 3.14, True, 7]


def reverseOrder():
    data_three.reverse()
    data_three.pop()
    count = 0
    for i in data_three:
        count += 1
        if count == 2:
            data_three[1] = "B"
    print("\t", data_three)


reverseOrder()

# Data4
print("\nData4")
data_four = {"name": "Joe", "age": 26, "active": True, "hourly_wage": 14.75}


def changeActive():
    data_four.update({"active": False})


changeActive()


def joePaycheck():
    hourlyWage = data_four.get("hourly_wage")
    paycheck = (hourlyWage * 40)
    print("\t", paycheck)


joePaycheck()


def addAddress():
    data_four.update({"address": "123 West Main Street"})
    print("\t", data_four)


addAddress()
