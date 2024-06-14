import calendar

year=int(input('Please enter the year you want\n'))
month=int(input('Please enter the month you want\n'))

print('****************************************************')
print(f'here is the calender of month {calendar.month_name[month]} in year {year}\n')
print(calendar.month(year,month,4))
