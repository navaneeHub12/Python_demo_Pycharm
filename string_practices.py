#Here we are going to see String operations and functions


#split()  Use to split the string with white space
str1 = 'something is better than nothing'
print('Length of String: ', len(str1))
print('Split the string into list: ', str1.split())   #default action: it split based on white space


#strip() trimming of white spaces from the string in both sides, use rstrip() and lstrip()
str2 = '        Plates full of cake        '
print('Strip result: ',str2.strip())
print('Right side strip result: ', str2.rstrip())
print('Left side strip result: ', str2.lstrip())

#find() finding sub strings from the main string
str3 = 'Earth is good source for living beings'
print('Finding words in the string: ', str3.find('beings'))
print('Finding words in desire values: ', str3.find('is',0,20))
print('Result for unavailable word: ', str3.find('ta'))

#upper() Change lower case to upper case
str3 = 'pranika'
print('Lower to Upper case result: ', str3.upper())
#islower -It returns Boolean value if the string is lower case
print(str3,'is Lower case result: ', str3.islower())
print(str3, 'is this Upper case: ', str3.isupper())

#lower() Change upper to lower case
str4 = 'NAVANEETHAKRISHNAN'
print('Upper to lower case result: ', str4.lower())
#isUpper -It returns Boolean value if the string is Upper case
print(str4, 'is Upper case result: ', str4.isupper())
print(str4, 'is this lower case: ', str4.islower())

#isdigit()
str5 = '8437925195'
print(str5, 'is this digit: ',str5.isdigit())
print(str5, 'is this alpha: ',str5.isalpha())
#isalnum()
print(str5, 'is this alphanumeric: ', str5.isalnum())

#isspace()
print(str4,' has any space: ', str4.isspace())
print(str1, 'has any space: ',str1.isspace())
str6 = ' '
print(str6,'has any space: ',str6.isspace())

#capitalize()
print(str1, '-capitalize after: ', str1.capitalize())

