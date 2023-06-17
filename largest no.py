#WAP to input three no.s and print the largest no. using nested if statements
a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
c=int(input("Enter 3rd number"))
if(a>b):
    if(a>c):
        print("a is largest no.")
elif(b>c):
    if(b>a):
        print("b is largest no.")
else:
    print("c is largest no.")               