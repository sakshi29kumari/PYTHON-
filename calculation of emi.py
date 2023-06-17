#WAP to calculate EMI using 
P=int(input("enter principle="))
R=float(input("enter rate="))
T=int(input("enter time="))
n=int(input("enter n="))
EMI=(P*R*(1+R)**n)/((1+R)**n-1)
print("EMI=",EMI)