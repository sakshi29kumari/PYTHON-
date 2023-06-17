#WAP to input a no. and check whether it is divisible by 5 as well as 3 using if else

num=int(input("enter a number:"))
if(num%3==0 and num%5==0):
    print("no. is divisible by both 3 and 5")
else:
    print("not divisible by any of the no. or both of the no.")