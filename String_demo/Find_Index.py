""" Write a program for Find() and Index() method"""

"""Program for Find() method"""

str1 = 'Navaneethakrishnan'
r1 = str1.find('a')

print('Result1: ', r1)

"""Program for Find() with parameter in the method"""

str2 = 'welcome'
r2 = str2.find('e',2,5)
print('Result2: ', r2)

"""Program for rfind() method"""
str3 = 'Hollywood'
r3 = str3.rfind('o')
print('Result: ', r3)

"""Program for index() method"""
str4 = 'Australia'
r4 = str4.index('t')
print('Result: ', r4)

"""Program for rindex() method"""
str5 = 'fantastic'
r5 = str5.rindex('a')
print('Result: ', r5)