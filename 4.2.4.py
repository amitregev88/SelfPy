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
    
