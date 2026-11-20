"""Write a program to find a String Literals"""

str = 'Krishnan'
print(str)
"""Print the given string in travesing method"""
for ch in str:
    print(ch)

"""Find length of string by len(st) method"""
print('Length of string:', len(str))

"""Print the given string using For loop range function"""
for i in range(len(str)):
    print(str[i])

"""Print the given string using indexing method"""
print('5th place char: ', str[5])