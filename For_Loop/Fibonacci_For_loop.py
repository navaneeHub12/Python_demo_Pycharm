# Write a program to find a Fibonacci series

n = int(input("Enter n number here: "))
a = 0
b = 1
print('Fib(',n,') is: ',a,b, end=" ")
for i in range(2, n+1):
    fib = a + b
    a = b
    b = fib
    print(fib, end=" ")



