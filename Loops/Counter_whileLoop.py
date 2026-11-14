#Write a program to split the given integer

inp_num = int(input('Enter your integer: '))

while inp_num > 0:
    reminder = inp_num % 10
    print(reminder)
    inp_num //= 10

print("End of while loop")