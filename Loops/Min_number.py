# Write a program to find a Min number from the input

n = int(input('How many number you want to compare: '))
i = 0
Min = 0
print('Enter the numbers here: ')
while i < n:
    i += 1
    x = int(input(''))
    if Min == 0:
        Min = x
    elif x < Min:
        Min = x
print('Minium number is: ', Min)
