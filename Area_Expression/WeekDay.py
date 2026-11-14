#Writen a program to find a weekday

week_day = int(input('Enter Week day number here: '))

if week_day == 0:
    print('Week day name: Monday')
elif week_day == 1:
    print('Week day name: Tuesday')
elif week_day == 2:
    print('Week day name: Wednesday')
elif week_day == 3:
    print('Week day name: Thursday')
elif week_day == 4:
    print('Week day nane is: Friday')
elif week_day == 5:
    print('Week day name is: Saturday')
elif week_day == 6:
    print('Week day name is: Sunday')
else:
    print('Enter Weekday number between 0 to 6')
