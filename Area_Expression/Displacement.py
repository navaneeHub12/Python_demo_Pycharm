#Write a program to find a displacement

#Displacement formula
# u initial velocity, v Final velocity, a Accelaration
# ((v*v) - (u*U) / (2 * a))

u = float(input('Enter Initial velocity: '))
v = float(input('Enter final velocity: '))
a = float(input('Enter Accelaration value: '))

dis = ((v*v) - (u*u) / (2 * a))

print('Displacement value is: ', dis)
