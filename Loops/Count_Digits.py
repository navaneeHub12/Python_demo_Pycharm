# Write a program to count digits for a given number

num = int(input("Enter your digits: "))

count = 0
while num > 0:
    num //= 10
    count += 1

print("Number of digits: ", count)

