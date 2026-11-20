""" Write a program for Alignment and Padding method"""

""" ljust() method"""
str1 = 'generous'
r1 = str1.ljust(12,'*')
print('Result1: ', r1)

""" rjust() method"""
str2 = 'automatic'
r2 = str2.rjust(12,'-')
print('Result2: ', r2)

""" center() method"""
str3 = 'honda'
r3 = str3.center(10,'$')
print('Result3: ', r3)

""" rstrip() method"""
r4 = r1.rstrip('*')
print('Result4: ', r4)

""" lstrip() method"""
r5 = r2.lstrip('-')
print('Result5: ', r5)

""" strip() method"""
str4 = '888umberlla888'
r6 = str4.strip('8')
print('Result6: ', r6)