import calendar

date = input("Enter a date (dd/mm/yyyy ):")
day = date[:2]
month = date[3:5]
year = date[6:]

res = calendar.weekday(int(year), int(month), int(day))

if res == 0:
    print("Monday")
elif res == 1:
    print("Tuesday")
elif res == 2:
    print("Wednesday")
elif res == 3:
    print("Thursday")
elif res == 4:
    print("Friday")
elif res == 5:
    print("Saturday")
else:
    print("Sunday")
    
"""
import calendar
date = input("Enter a date: ")
day = int(date[:2])
month = int(date[3:5])
year = int(date[6:])
weekday=calendar.weekday(year,month,day)
if weekday == 0:
    print("Monday")
if weekday == 1:
    print("Tuesday")
if weekday == 2:
    print("Wednesday")
if weekday == 3:
    print("Thursday")
if weekday == 4:
    print("Friday")
if weekday == 5:
    print("Saturday")
if weekday == 6:
    print("Sunday")
    """