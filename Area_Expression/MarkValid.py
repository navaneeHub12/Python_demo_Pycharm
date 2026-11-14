#Write a program to find a valid mark for three subject

math = int(input('Enter Math mark: '))
science = int(input('Enter Science mark: '))
english = int(input('Enter English mark: '))

passMark = 35
invalidMark = 101



if (math >= passMark) and (science >= passMark) and (english >= passMark):
    print('Result: Pass')
elif (math >= invalidMark) and (science >= invalidMark) and (english >= invalidMark):
    print('Enter valid marks')
else:
    print('Result: Fail')

