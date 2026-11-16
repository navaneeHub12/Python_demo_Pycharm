"""Write a program to display a credit card - mask the first 12 digits"""

card_no = input('Enter your credit card number: ')
str4 = card_no[15:19]

print('X' * 4, 'X' * 4, 'X' * 4, str4)
