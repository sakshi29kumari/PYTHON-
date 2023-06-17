#WAP to input an operator and two no. and based on operator perform the operations b/w two no.s
#e.g. if operator is'+', then print the addition of two no.s and so on..

num1=int(input("enter 1st no."))
num2=int(input("enter 2nd no."))
op=input("enter the operator")
if(op=='+'):
    print(num1+num2)
elif(op=='-'):
    print(num1-num2)
elif(op=='*'):
    print(num1*num2)
else:
    print(num1/num2)   
