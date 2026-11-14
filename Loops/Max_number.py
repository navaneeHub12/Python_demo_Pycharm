# Write a program to find a Max number from input

n = 5
i = 0
max = 0
print("Enter 5 number here: ")
while i < 5:
    i += 1
    x = int(input(''))
    if x > max:
        max = x
print('Maximum is: ', max)
