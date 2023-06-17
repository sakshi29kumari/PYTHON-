#WAP to print area of triangle using heron's formula by taking all sidesas input
a=int(input("enter 1st side="))
b=int(input("enter 2nd side="))
c=int(input("enter 3rd side="))
s=(a+b+c)/2
from math import *
area=(sqrt(s*(s-a)*(s-b)*(s-c)))
print("area of triangle=",area)
