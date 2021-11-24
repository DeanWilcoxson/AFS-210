class Employee:
    def __init__(self, first=None, last=None, id=None, pay=0.00):
        self.firstName = first
        self.lastName = last
        self.employeeID = id
        self.hourlyPay = pay

    def setFirstName(self, first):
        self.firstName = first

    def getFirstName(self):
        return self.firstName

    def setLastName(self, last):
        self.lastName = last

    def getLastName(self):
        return self.lastName
    
    def setEmployeeID(self, id):
        self.employeeID = id

    def getEmployeeID(self):
        return self.employeeID
    
    def setHourlyPay(self, pay):
        self.hourlyPay = pay

    def getHourlyPay(self):
        return self.hourlyPay

    def pay(self, hoursWorked):
        if(hoursWorked <= 40.0):
            return self.hourlyPay * hoursWorked
        else: 
            weeklyPay = self.hourlyPay * 40
            weeklyPay += (self.hourlyPay * 1.5) * (hoursWorked - 40)
            return weeklyPay    

employeeId = int(input("Enter The Employee's ID number: "))
fName = str(input("Enter The Employee's First Name: "))
lName = str(input("Enter The Employee's Last Name: "))
hourlyWage = float(input("Enter The Employee's Hourly Wage: "))
hoursWorked = float(input("How many hours did " + fName + " " + lName + " work this week? "))

newEmployee = Employee(fName,lName,employeeId,hourlyWage)
paycheckAmount = newEmployee.pay(hoursWorked)
print("{0} {1}'s paycheck is ${2:.2f}".format(newEmployee.getFirstName(),newEmployee.getLastName(),paycheckAmount))