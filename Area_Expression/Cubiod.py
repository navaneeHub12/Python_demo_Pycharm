#Write a program to find an area of Cubiod

#cubiod formula
# (2 * (length * height) +  (length * breadth) + (height * breadth))

length = float(input('Enter length value: '))
height = float(input('Enter Height value: '))
breadth = float(input('Ehter breadth value: '))

area = 2 * ((length * height) + (length * breadth) + (height * breadth))

print('Area of a cuboid is: ', area)
