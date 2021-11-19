class Employee():
    employeeId = int(input("Enter The Employee's ID number: "))
    fName = str(input("Enter The Employee's First Name: "))
    lName = str(input("Enter The Employee's Last Name: "))
    hourlyWage = float(input("Enter The Employee's Hourly Wage: "))
    hoursWorked = float(input("How many hours did " + fName + " " + lName + " work this week? "))

    def pay(employeeId, fName, lName, hourlyWage, hoursWorked):
        paycheck = str((float(hoursWorked)) * float(hourlyWage))

        if(hoursWorked <= 40.0):
            print(fName + " " + lName + "'s paycheck amount is $" + paycheck)

        elif(hoursWorked > 40.0):
            hourlyWage = hourlyWage * 1.5
            timeAndAHalf = hoursWorked - 40.0
            overtime = timeAndAHalf * hourlyWage
            bonusPay = str(float(paycheck) + float(overtime))
            print(fName + " " + lName + "'s paycheck amount is $" + bonusPay)


Employee.pay(Employee.employeeId, Employee.fName, Employee.lName, Employee.hourlyWage, Employee.hoursWorked)
