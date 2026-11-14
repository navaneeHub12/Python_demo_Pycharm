# Write a program to sum of n numbers

n = int(input('Enter your number here: '))
sum = 0

for i in range(1,n+1):
    sum += i

print('Sum of ',n,'numbers: ', sum)
