# Write a program for Factorial by using For loop

n = int(input('Enter n number: '))
fact = 1
for i in range(1,n+1):
    fact *= i
print("Factorial for",n,"number is: ", fact)