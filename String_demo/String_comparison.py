""" Write a program to compare two strings"""

str1 = 'apple'
str2 = 'apply'

r1 = str1 < str2
print('Result1: ', r1)

str3 = '3rd'
str4 = 'York'
r2 = str3 > str4
print('Result2: ', r2)

str5 = 'same'
str6 = 'same'
r3 = (str5 == str6)
print('Result3: ', r3)

str7 = 'Honda'
str8 = 'Tata'
r4 = (str7 != str8)
print('Result4: ',r4)

str9 = 'Navaneethakrishnan'
print('Result5:', 'a' in str9)

print('Result6: ', 'zy' in str9)

print('Result7: ', 'cw' not in str9)


