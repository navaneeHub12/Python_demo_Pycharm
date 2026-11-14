# Write a program to find a Factor number

n = int(input('Enter your number here: '))
print('Factor for',n,'is: ')
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")

