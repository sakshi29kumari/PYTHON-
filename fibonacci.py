#WAP to print following fibonacci series using for loop:
# 0 1 1 2 3 5 8 13
a=0
b=1
print(a)
print(b)
for i in range(0,6):
    c=a+b
    print(c)
    a=b
    b=c
    