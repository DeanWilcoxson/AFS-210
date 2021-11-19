class Employee():
    def pay():
        employeeId = int(input("Please Enter The Employee's ID number: "))
        fName = str(input("Please Enter The Employee's First Name: "))
        lName = str(input("Please Enter The Employee's Last Name: "))
        hourlyWage = float(input("Please Enter The Employee's Hourly Wage: "))
        hoursWorked = float(
            input("How many hours did " + fName + " " + lName + " work this week? "))
        paycheck = str(hoursWorked * hourlyWage)
        if(hoursWorked <= 40.0):
            print(fName + " " + lName + "'s paycheck amount is $" + paycheck)
        elif(hoursWorked > 40.0):
            timeAndAHalf = hoursWorked - 40.0
            hourlyWage = hourlyWage * 1.5
            overtime = timeAndAHalf * hourlyWage
            bonusPay = str(paycheck + overtime)
            print(fName + " " + lName + "'s paycheck amount is $" + bonusPay)
Employee.pay()