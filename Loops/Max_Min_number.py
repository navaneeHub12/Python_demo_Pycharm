# Write a program to find a Min and Max number from the given input

n = int(input('How many number want to enter: '))
i = 0
Max = 0
Min = 0

while i < n:
    i += 1
    x = int(input(''))
    if x > Max:
        Max = x
    elif Min == 0:
        Min = x
    elif x < Min:
        Min = x
print('Maximum number is: ', Max)
print('Minimum number is: ', Min)