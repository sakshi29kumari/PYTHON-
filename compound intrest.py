#WAP to print compound intrest
P=int(input("enter principle="))
R=float(input("enter rate="))
T=int(input("enter time="))
n=int(input("enter n="))
A=P*(1+(R/n))**n*T
CI=A-P
print("Compound intrest=",CI)