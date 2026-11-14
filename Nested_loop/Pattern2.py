# Write a program to print a pattern 2 right angle triangle

print('*** Right angle triangle ***')

for i in range(1,6):
    for j in range(1, i+1):
        print('*', end= ' ')
    print('')