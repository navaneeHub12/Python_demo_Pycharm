#Write a program to check a gender

gender = input('Enter Male or Female: ')

if (gender == 'Male') or (gender == 'male'):
    print('Gender is Male')
elif (gender == 'Female') or (gender == 'female'):
    print('Gender is Female')
else:
    print('Enter only Male or Female')

