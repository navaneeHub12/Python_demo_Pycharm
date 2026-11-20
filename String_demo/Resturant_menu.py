"""Write a program to display a Restaurant menu """

item1 = 'Dosa'
item2 = 'Idly'
item3 = 'Butter Dosa'
item4 = 'Sambar Vada'

price1 = '$50'
price2 = '$30'
price3 = '$60'
price4 = '$20'
gap_length = 20

gap1 = gap_length - (len(item1) - len(price1))
gap2 = gap_length - (len(item2) - len(price2))
gap3 = gap_length - (len(item3) - len(price3))
gap4 = gap_length - (len(item4) - len(price4))

print(item1,'-' * gap1,price1)
print(item2,'-' * gap2,price2)
print(item3,'-' * gap3,price3)
print(item4,'-' * gap4,price4)

