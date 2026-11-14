#Write a program to find a number is Palindrome after reverse

digits = int(input('Enter a digits: '))

rev = 0
copy_digits = digits

while digits > 0:
    reminder = digits % 10
    rev = rev * 10 + reminder
    digits //= 10

if rev == copy_digits:
    print("Given digits is a Palindrome")
else:
    print("Given digits is not a Palindrome")