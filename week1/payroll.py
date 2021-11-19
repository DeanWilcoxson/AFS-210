class Employee():
    # def __init__(self, fName, lName, employeeId, hourlyWage):
    #     super(Employee, self).__init__(fName, lName, employeeId, hourlyWage)

    fName = str(input("Please Enter The Employee's First Name: "))
    lName = str(input("Please Enter The Employee's Last Name: "))
    employeeId = int(input("Please Enter The Employee's ID number: "))
    hourlyWage = float(input("Please Enter The Employee's Hourly Wage: "))
    
    def pay(self, hoursWorked):
        paycheck = hoursWorked * self.hourlyWage
        paycheck.type = float
        if(hoursWorked <= 40.0):
            return paycheck
