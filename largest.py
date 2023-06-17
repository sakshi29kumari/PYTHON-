#WAP to input three no. and print the largest one

a=int(input("enter 1st no."))
b=int(input("enter 2nd no."))
c=int(input("enter 3rd no."))
if(a>b and a>c):
    print("1st no is largest")
elif(b>a and b>c):
    print("2nd no is largest")
else:
     print("3rd no is largest")