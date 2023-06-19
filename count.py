#WAP to input a string and count the no. of upper case and lower case letters
str1=input("enter a string")
ucase,lcase=0,0
for ch in str1:
    if ch>='A' and ch<="Z":
        ucase+=1
    if ch>='a' and ch<='z':
        lcase+=1
print("no. of upper case letters:",ucase)
print("no. of lower case letters:",lcase)

        
