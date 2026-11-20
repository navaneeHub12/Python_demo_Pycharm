""" Write a program to find a palindrome string"""

str1 = input('Enter your string: ')
str2 = str1.lower()
""" We can use casefold() method for changing case"""
#print(str2)
str3 = str2.replace(' ','')
#print(str3)
str4 = str3[::-1]
#print(str4)
if str4 == str3:
    print(str1)
else:
    str5 = str2+str4
    print(str5)