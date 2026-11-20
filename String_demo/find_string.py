""" Write a program using find() method """


str1 = 'nava,krishna,karthika'

str2 = str1[:str1.find(',')]
print(str2)

str3 = str1.find(',')
print(str3)
str4 = str1.find(',',str3+1)
print(str4)
sec_name = str1[str3+1:str4]
print(sec_name)
last_name = str1[str4+1:]
print(last_name)