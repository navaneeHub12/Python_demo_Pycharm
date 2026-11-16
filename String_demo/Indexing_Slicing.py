"""Write a program for Indexing and Slicing a string"""

str1 = 'Good Evening'
"""str1[start:stop:step]"""

#print(str1[0])
"""str1[index]"""

#print(str1[0:4])
"""Result - Good"""

#print(str1[::])
"""Result - Good Evening"""

#print(str1[2:8])
"""Result - od Eve"""

#print(str1[-7:])
"""Result - Evening"""

#str2 = str1[::-1]
#print(str2)
"""Result - gninevE dooG"""

str3 = str1[:-8:-1]
print(str3)
"""Result - gninevE"""



