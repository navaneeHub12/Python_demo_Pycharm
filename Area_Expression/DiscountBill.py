#Write a program to calculate a discount amount on the bill
#0 to 1000 - 10%
#1001 to 5000 - 15%
#5001 to 10000 - 20%
#10,001 and above - 25%

amt = int(input("Enter Bill amount: "))

if amt <= 1000:
    dis1 = amt * 0.1   #10%
    amt -= dis1
    print("10% discount is applied on the bill: ", amt)
elif (amt >=1001) and (amt <= 5000):
    dis2 = amt * 0.15   #15%
    amt -= dis2
    print("15% discount is applied on the bill: ", amt)
elif (amt >= 5001) and (amt <= 10_000):
    dis3 = amt * 0.20   #20%
    amt -= dis3
    print("20% discount is applied on the bill: ", amt)
elif amt >= 10_001:
    dis4 = amt * 0.25
    amt -= dis4
    print("25% discount is applied on the bill: ", amt)
else:
    print('Invalid amount')


