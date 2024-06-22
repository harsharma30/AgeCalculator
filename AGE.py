from datetime import date
Months={
    1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31
}

def IsLeapYear(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def NumOfDays(date1,date2):
    return(date2 - date1).days

print("Date Format:dd/mm/yyyy")
day1,mon1,year1=input("Please Enter Your Birthdate: ").split('/')
day2,mon2,year2=input("Please Enter The Current Date: ").split('/')

date1=date(int(year1),int(mon1),int(day1))
date2=date(int(year2),int(mon2),int(day2))

TotalDays=NumOfDays(date1,date2)

if int(year1)==int(year2):
    month = TotalDays/30
    day=TotalDays%30
    year=0
else:
    year=TotalDays/365
    month=(TotalDays%365)/30


    if IsLeapYear(int(year1)):
        Months[2]=29

    if int(day2)>=int(day1):
        day=int(day2)-int(day1)
    elif int(mon2)==2 and (IsLeapYear(int(year2)) or (not IsLeapYear(int(year2)))):
        year=year-1
        month=11
        prevMonth=Month[int(mon2)-1]
        days=prevMonth-int(day1)+int(day2)
        day=days
    else:
        prevMonth=Months[int(mon2)-1]
        days=prevMonth-int(day1)+int(day2)
        day=days
print("Your Age is:",int(year),"years ",int(month),"month ",int(day),"days")
