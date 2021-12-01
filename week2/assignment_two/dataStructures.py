# Tasks:

# Data 1
Data1 = (7, False, "Apple", True, 7, 98.6)
# Data1 - Count the number of items
print(len(Data1))
# Data1 - Find the value of the fourth item stored in the data set
print(Data1[3])
# Data1 - Count the number of times 7 appears
print(Data1.count(7))


# Data 2
Data2 = {"July", 4, 8, "Tango", 4.3, "Bingo"}
# Data2 - Remove a random element from the data set
Data2.pop()
# Data2 - Add "Alpha" to the data set
Data2.add("Alpha")
# Data2 - Print data set
print(Data2)


# Data 3
Data3 = ["A", 7, -1, 3.14, True, 7]
# Data3 - Print the data set in reverse order
Data3.reverse()
print(Data3)
# Data3 - Change the second value in the data set to ‘B’
Data3[1] = "B"
# Data3 - Remove the last item and print the data set
Data3.pop()
print(Data3)


# Data 4
Data4 = {"name": "Joe",  "age": 26,   "active": True,  "hourly_wage": 14.75}
# Data4 - Change "active" to False
Data4.update({"active": False})
# Data4 - Add "address" with a value of "123 West Main Street"
Data4.update({"address": "123 West Main Street"})
# Data4 - Print the weekly salary for Joe if he worked a full 40 hour week.
print(Data4.get("hourly_wage")*40)
# Data4 - Print the data set
print(Data4)
