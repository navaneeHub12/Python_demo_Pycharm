#Write a program to find a Gender

gender = input('Enter male or female: ')
tolower_input = gender.lower()

if tolower_input == 'male':
    print('Gender is Male')
elif tolower_input == 'female':
    print('Gender is Female')
else:
    print('Enter only Male and Female')
