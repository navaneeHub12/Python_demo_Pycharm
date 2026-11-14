#Write a program for reverse a given digits

digits = int(input('Enter your digits: '))

rev = 0
while digits > 0:
    reminder = digits % 10
    rev = rev * 10 + reminder
    digits //= 10
print("Reverse a digits: ", rev)