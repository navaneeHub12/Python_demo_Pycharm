#Write a program to find a Prime number from 1 to 100
n = int(input('Enter n value here: '))
for i in range(1,n+1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i, end=" ")
print('\n')


