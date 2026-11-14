#Write a program to show Multiplication for given number

Mul_input = int(input('Enter Multiplication number: '))

counter = 0

while counter < 16:
    counter += 1
    print(Mul_input, 'X', counter, '=', Mul_input * counter)

print("**** End of Multiplication ****")