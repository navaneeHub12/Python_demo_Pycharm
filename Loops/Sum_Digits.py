#Write a program to sum of digits a number

digs = int(input('Enter your digits: '))

sum = 0

while digs > 0:
    reminder = digs % 10
    sum += reminder
    digs //= 10
print("Sum of digits: ", sum)