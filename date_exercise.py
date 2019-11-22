from datetime import datetime, timedelta

curr_dt = datetime.now()
print(f'todat is {str(curr_dt)}')

today = datetime.now()
one_day = timedelta(days=1)
yeserterday = today - one_day
print(f'yeserterday is {str(yeserterday)}')

one_week = timedelta(weeks=1)
lastweek = today - one_week
print(f'last week is {str(lastweek)}')

print(f'Day: {str(today.day)}')
print(f'Month: {str(today.month)}')
print(f'Year: {str(today.year)}')

print(f'Hour: {str(today.hour)}')
print(f'Minute: {str(today.minute)}')
print(f'Second: {str(today.second)}')

birthday = input('Please enter your birthday (dd/mm/yyyy)')
birtherday_dt = datetime.strptime(birthday, '%d/%m/%Y')
print(f'Your Birthday: {str(birtherday_dt)}')